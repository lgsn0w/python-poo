#!/usr/bin/env python3
"""Dependency-free Markdown -> PDF for the Teoria-POO handouts.
Uses only the 14 standard PDF fonts (no embedding), does its own line
wrapping/pagination. Subset: #/##/### headings, ```fenced code```, - and N.
lists, > blockquotes, --- rules, **bold**, `inline code`. Portuguese accents
via WinAnsi/cp1252."""
import re
import sys

PW, PH = 595.28, 841.89          # A4
LEFT, RIGHT, TOP, BOTTOM = 56, 56, 56, 60
USABLE = PW - LEFT - RIGHT
FONTS = {"normal": "F1", "bold": "F2", "code": "F3", "obl": "F4"}

NARROW = " iIl.,:;!|'ijtf()[]{}"
WIDE = "mMwW@%"


def gw(ch, size, style):
    if style == "code":
        return 0.6 * size
    if ch in NARROW:
        f = 0.30
    elif ch in WIDE:
        f = 0.90
    elif ch.isupper():
        f = 0.70
    elif ch.isdigit():
        f = 0.56
    else:
        f = 0.52
    return f * size


def word_w(word, size, style):
    return sum(gw(c, size, style) for c in word)


# ---------- inline + block parsing ----------
INLINE = re.compile(r"`([^`]+)`|\*\*([^*]+)\*\*")


def inline(text):
    runs, pos = [], 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            runs.append((text[pos:m.start()], "normal"))
        if m.group(1) is not None:
            runs.append((m.group(1), "code"))
        else:
            runs.append((m.group(2), "bold"))
        pos = m.end()
    if pos < len(text):
        runs.append((text[pos:], "normal"))
    return runs or [("", "normal")]


def parse_blocks(md):
    lines = md.split("\n")
    blocks, i = [], 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        if stripped.startswith("```"):
            indent = len(line) - len(stripped)
            i += 1
            code = []
            while i < len(lines) and not lines[i].lstrip().startswith("```"):
                code.append(lines[i][indent:] if lines[i][:indent].isspace()
                            or lines[i][:indent] == "" else lines[i].lstrip())
                i += 1
            i += 1
            blocks.append(("code", code))
            continue

        if re.match(r"^---+\s*$", line):
            blocks.append(("hr",))
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            blocks.append(("h", len(m.group(1)), inline(m.group(2))))
            i += 1
            continue

        if line.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            blocks.append(("quote", inline(" ".join(q))))
            continue

        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            blocks.append(("ol", m.group(1), inline(m.group(2))))
            i += 1
            continue

        m = re.match(r"^[-*]\s+(.*)$", line)
        if m:
            blocks.append(("ul", None, inline(m.group(1))))
            i += 1
            continue

        if line.strip() == "":
            i += 1
            continue

        # continuation of previous list item / paragraph
        if (re.match(r"^\s+\S", line) and blocks
                and blocks[-1][0] in ("ol", "ul", "p")):
            b = blocks[-1]
            extra = inline(" " + line.strip())
            blocks[-1] = b[:-1] + (b[-1] + extra,)
            i += 1
            continue

        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() != "" and not re.match(
                r"^(#{1,6}\s|```|---+\s*$|>|\d+\.\s|[-*]\s)", lines[i].lstrip()):
            para.append(lines[i].strip())
            i += 1
        blocks.append(("p", inline(" ".join(para))))
    return blocks


def wrap_runs(runs, size, max_w):
    words = []
    for text, style in runs:
        for tok in text.split(" "):
            if tok:
                words.append((tok, style))
    lines, cur, curw = [], [], 0.0
    sw = gw(" ", size, "normal")
    for word, style in words:
        ww = word_w(word, size, style)
        add = ww + (sw if cur else 0)
        if cur and curw + add > max_w * 0.99:
            lines.append(cur)
            cur, curw = [(word, style)], ww
        else:
            cur.append((word, style))
            curw += add
    if cur:
        lines.append(cur)
    return lines or [[]]


def esc(s):
    b = s.encode("cp1252", "replace")
    return b.replace(b"\\", b"\\\\").replace(b"(", b"\\(").replace(b")", b"\\)")


# ---------- renderer ----------
class PDF:
    def __init__(self):
        self.pages = []
        self.ops = bytearray()
        self.y = PH - TOP

    def newpage(self):
        self.pages.append(self.ops)
        self.ops = bytearray()
        self.y = PH - TOP

    def show(self, x, y, font, size, text, gray=0.0):
        if gray:
            self.ops += f"{gray:.2f} {gray:.2f} {gray:.2f} rg ".encode("ascii")
        self.ops += f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ".encode("ascii")
        self.ops += b"(" + esc(text) + b") Tj ET"
        self.ops += b" 0 0 0 rg\n" if gray else b"\n"

    def rect(self, x, y, w, h, gray):
        self.ops += (f"{gray:.2f} {gray:.2f} {gray:.2f} rg {x:.2f} {y:.2f} "
                     f"{w:.2f} {h:.2f} re f 0 0 0 rg\n").encode("ascii")

    def hline(self, x1, x2, y, gray, width=0.6):
        self.ops += (f"{gray:.2f} {gray:.2f} {gray:.2f} RG {width} w {x1:.2f} "
                     f"{y:.2f} m {x2:.2f} {y:.2f} l S 0 0 0 RG\n").encode("ascii")

    def draw_line(self, line, x0, baseline, size, fmap, gray=0.0):
        sw = gw(" ", size, "normal")
        x = x0
        for i, (word, style) in enumerate(line):
            if i:
                x += sw
            self.show(x, baseline, fmap[style], size, word, gray)
            x += word_w(word, size, style)

    def flow(self, runs, size, leading, fmap, space_before=3, indent=0,
             gray=0.0, marker=None, marker_style="normal", hang=0):
        wl = wrap_runs(runs, size, USABLE - indent)
        self.y -= space_before
        for i, line in enumerate(wl):
            if self.y - leading < BOTTOM:
                self.newpage()
            baseline = self.y - size
            if i == 0 and marker is not None:
                self.show(LEFT + indent - hang, baseline,
                          FONTS[marker_style], size, marker)
            self.draw_line(line, LEFT + indent, baseline, size, fmap, gray)
            self.y -= leading

    def heading(self, level, runs):
        size = {1: 17, 2: 13.5, 3: 11.5}.get(level, 11)
        lead = {1: 22, 2: 18, 3: 15}.get(level, 15)
        before = {1: 12, 2: 15, 3: 11}.get(level, 10)
        hmap = {"normal": "F2", "bold": "F2", "code": "F3", "obl": "F2"}
        if self.y - (lead + before) < BOTTOM:
            self.newpage()
        self.flow(runs, size, lead, hmap, space_before=before)
        if level == 1:
            self.y += 2
            self.hline(LEFT, LEFT + USABLE, self.y, 0.55, 1.2)
            self.y -= 6

    def code_block(self, code):
        size, lead, pad = 8.5, 12, 6
        maxc = max(1, int((USABLE - 2 * pad) / (0.6 * size)))
        wrapped = []
        for ln in code:
            if len(ln) <= maxc:
                wrapped.append(ln)
            else:
                while ln:
                    wrapped.append(ln[:maxc])
                    ln = ln[maxc:]
        self.y -= 5
        h = pad * 2 + lead * len(wrapped)
        if h <= (PH - TOP - BOTTOM) and self.y - h < BOTTOM:
            self.newpage()
        if self.y - h >= BOTTOM:
            self.rect(LEFT, self.y - h, USABLE, h, 0.95)
            for i, wl in enumerate(wrapped):
                base = self.y - pad - size - i * lead
                self.show(LEFT + pad, base, "F3", size, wl)
            self.y -= h + 3
        else:  # taller than a page: split, no background
            for wl in wrapped:
                if self.y - lead < BOTTOM:
                    self.newpage()
                self.show(LEFT + pad, self.y - size - 2, "F3", size, wl)
                self.y -= lead
            self.y -= 3

    def quote(self, runs):
        size, lead, ind = 10, 14, 16
        wl = wrap_runs(runs, size, USABLE - ind - 6)
        self.y -= 5
        qmap = {"normal": "F4", "bold": "F2", "code": "F3", "obl": "F4"}
        top = self.y
        for line in wl:
            if self.y - lead < BOTTOM:
                self.rect(LEFT + 2, self.y + 2, 2.2, top - self.y - 2, 0.6)
                self.newpage()
                top = self.y
            self.draw_line(line, LEFT + ind, self.y - size, size, qmap, 0.35)
            self.y -= lead
        self.rect(LEFT + 2, self.y + lead - size, 2.2,
                  top - (self.y + lead - size), 0.6)
        self.y -= 3

    def render(self, blocks):
        for b in blocks:
            t = b[0]
            if t == "h":
                self.heading(b[1], b[2])
            elif t == "p":
                self.flow(b[1], 10.5, 14.5, FONTS, space_before=4)
            elif t == "code":
                self.code_block(b[1])
            elif t == "quote":
                self.quote(b[1])
            elif t == "hr":
                self.y -= 9
                if self.y < BOTTOM:
                    self.newpage()
                self.hline(LEFT, LEFT + USABLE, self.y, 0.7, 0.6)
                self.y -= 9
            elif t == "ol":
                self.flow(b[2], 10.5, 14.5, FONTS, space_before=3,
                          indent=20, marker=b[1] + ".", hang=20)
            elif t == "ul":
                self.flow(b[2], 10.5, 14.5, FONTS, space_before=3,
                          indent=20, marker="•", hang=20)
        self.pages.append(self.ops)

    def build(self):
        obj, buf = {}, bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")

        def add(num, body):
            obj[num] = len(buf)
            buf.extend(f"{num} 0 obj\n".encode("ascii"))
            buf.extend(body)
            buf.extend(b"\nendobj\n")

        n = len(self.pages)
        add(1, b"<< /Type /Catalog /Pages 2 0 R >>")
        kids = " ".join(f"{7 + 2 * k} 0 R" for k in range(n))
        add(2, f"<< /Type /Pages /Kids [{kids}] /Count {n} >>".encode("ascii"))
        for num, base in ((3, "Helvetica"), (4, "Helvetica-Bold"),
                          (5, "Courier"), (6, "Helvetica-Oblique")):
            add(num, (f"<< /Type /Font /Subtype /Type1 /BaseFont /{base} "
                      f"/Encoding /WinAnsiEncoding >>").encode("ascii"))
        for k, ops in enumerate(self.pages):
            pn, cn = 7 + 2 * k, 8 + 2 * k
            add(pn, (f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PW} {PH}] "
                     f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R "
                     f"/F4 6 0 R >> >> /Contents {cn} 0 R >>").encode("ascii"))
            add(cn, f"<< /Length {len(ops)} >>\nstream\n".encode("ascii")
                + bytes(ops) + b"\nendstream")
        maxn = 6 + 2 * n
        xref = len(buf)
        buf.extend(f"xref\n0 {maxn + 1}\n".encode("ascii"))
        buf.extend(b"0000000000 65535 f \n")
        for num in range(1, maxn + 1):
            buf.extend(f"{obj[num]:010d} 00000 n \n".encode("ascii"))
        buf.extend((f"trailer\n<< /Size {maxn + 1} /Root 1 0 R >>\n"
                    f"startxref\n{xref}\n%%EOF").encode("ascii"))
        return bytes(buf)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        blocks = parse_blocks(f.read())
    pdf = PDF()
    pdf.render(blocks)
    with open(sys.argv[2], "wb") as f:
        f.write(pdf.build())
    print("wrote", sys.argv[2], f"({len(pdf.pages)} pages)")
