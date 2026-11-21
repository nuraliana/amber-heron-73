"""news-image-20261121 round 4: copy the pre-rendered front page to output.

The entry image (entry.png, 35 stories from Saturday 21 November 2026,
7 regions) is rendered in the repository. This program only copies it to
$MAKEFUN_OUTPUT_DIR/entry.png using the standard library, so it runs in
the grader's stdlib-only image with no network and no fonts.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

os.makedirs(OUT, exist_ok=True)
with open(SRC, "rb") as f:
    magic = f.read(8)
if magic != PNG_MAGIC:
    sys.exit("entry.png is not a PNG file")
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
print(f"wrote entry.png ({os.path.getsize(SRC)} bytes)")
