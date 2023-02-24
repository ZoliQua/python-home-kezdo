# Create a precise "Crack the Code" poster that exactly matches the user's specification.

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1200, 1800  # overall canvas
UPPER_H = 620      # upper part height with clear separation
LOWER_H = H - UPPER_H

img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Try to load a clean sans font; fall back to default if needed.
def load_font(size):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    ]:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            continue
    return ImageFont.load_default()

title_font = load_font(140)
label_font = load_font(36)
digit_font = load_font(120)
legend_font = load_font(36)

# Colors
BLACK = (30, 30, 30)
BLUE = (20, 110, 200)
GREEN = (35, 160, 70)
RED = (220, 45, 45)
PURPLE = (80, 50, 160)
GOLD = (245, 205, 70)
DARK_GOLD = (160, 130, 30)
GREY = (70, 70, 70)

# --- Upper part layout ---
left_x0, left_y0 = 40, 40
left_x1, left_y1 = W//2 - 20, UPPER_H - 20  # left section
right_x0, right_y0 = W//2 + 20, 40
right_x1, right_y1 = W - 40, UPPER_H - 20   # right section

# Left section contains: lock (top) and legend (bottom)
lock_box = (left_x0, left_y0, left_x1, left_y0 + (left_y1-left_y0)//2 - 10)
legend_box = (left_x0, lock_box[3] + 20, left_x1, left_y1)

# Draw lock (simplified, hand-drawn style)
def draw_lock(draw, box):
    x0, y0, x1, y1 = box
    w = x1 - x0
    h = y1 - y0
    body_h = int(h * 0.58)
    shackle_h = h - body_h
    # Shackle
    shack_w = int(w * 0.58)
    shack_x = x0 + (w - shack_w)//2
    shack_y = y0
    shack_r = int(min(shack_w, shackle_h*1.3)/2)
    # outer shackle
    draw.rounded_rectangle([shack_x, shack_y, shack_x+shack_w, shack_y+shackle_h], radius=shack_r, outline=BLACK, width=6)
    # body
    body_y0 = y0 + shackle_h + 5
    body_y1 = y1
    draw.rounded_rectangle([x0+6, body_y0, x1-6, body_y1], radius=20, fill=GOLD, outline=BLACK, width=6)
    # question marks
    q_font = load_font(int((body_y1 - body_y0) * 0.55))
    q_text = "???"
    tw, th = draw.textbbox((0,0), q_text, font=q_font)[2:]
    tx = x0 + (w - tw)//2
    ty = body_y0 + (body_y1 - body_y0 - th)//2 - 5
    draw.text((tx, ty), q_text, font=q_font, fill=RED)

draw_lock(draw, lock_box)

# Draw legend box
def draw_legend(draw, box):
    x0, y0, x1, y1 = box
    draw.rectangle([x0, y0, x1, y1], outline=BLACK, width=5)
    pad = 20
    cx = x0 + pad + 14
    cy = y0 + pad + 14
    r = 14
    # three lines
    items = [
        (RED, "Nothing is correct"),
        (BLUE, "Right #, wrong place"),
        (GREEN, "Right #, right place"),
    ]
    line_gap = 18
    for color, text in items:
        # dot
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color, outline=None)
        # text
        draw.text((cx+20, cy-14), text, font=legend_font, fill=BLACK)
        cy += 2*r + line_gap

draw_legend(draw, legend_box)

# Right section: big title "CRACK THE CODE!"
title = "CRACK\nTHE\nCODE!"
# Fit title within right section bounds
def draw_multiline_centered(text, box, font, color):
    x0,y0,x1,y1=box
    # adapt font size to fit height
    # try decreasing size until it fits
    fsize = 160
    while True:
        f = load_font(fsize)
        bbox = draw.multiline_textbbox((0,0), text, font=f, spacing=10, align="center")
        tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
        if tw <= (x1-x0) - 20 and th <= (y1-y0) - 20:
            break
        fsize -= 2
        if fsize < 60:
            break
    tx = x0 + ((x1-x0) - tw)//2
    ty = y0 + ((y1-y0) - th)//2
    draw.multiline_text((tx, ty), text, font=f, fill=color, spacing=10, align="center")

draw_multiline_centered(title, (right_x0, right_y0, right_x1, right_y1), title_font, BLUE)

# --- Lower part: rows of dots -> numbers, no borders ---
# Gap between upper and lower
divider_y = UPPER_H
# We'll leave a small gap
row_area_y0 = divider_y + 20
row_area_y1 = H - 20
row_h = (row_area_y1 - row_area_y0) // 5

left_col_x0 = 60
left_col_x1 = 460   # dots column width
right_col_x0 = 520
right_col_x1 = W - 60

def draw_row(row_idx, dots, numbers):
    y_top = row_area_y0 + row_idx * row_h
    y_center = y_top + row_h//2
    # Draw the three dots horizontally
    dot_r = 24
    gap = 38
    start_x = left_col_x0 + 30
    for i, color in enumerate(dots):
        cx = start_x + i*(2*dot_r + gap)
        cy = y_center
        draw.ellipse([cx-dot_r, cy-dot_r, cx+dot_r, cy+dot_r], fill=color, outline=None)
    # Draw the three numbers with spaces
    nums_text = " ".join(numbers)
    # adjust font size to fit
    f = digit_font
    # compute bbox for current font
    tw, th = draw.textbbox((0,0), nums_text, font=f)[2:]
    # shrink if needed
    while tw > (right_col_x1 - right_col_x0):
        size = f.size - 2 if hasattr(f, "size") else 110
        f = load_font(size)
        tw, th = draw.textbbox((0,0), nums_text, font=f)[2:]
        if size < 60: break
    tx = right_col_x0 + ((right_col_x1 - right_col_x0) - tw)//2
    ty = y_center - th//2 - 5
    draw.text((tx, ty), nums_text, font=f, fill=PURPLE)

rows = [
    ([RED, RED, RED], ["2","6","8"]),
    ([RED, RED, RED], ["8","2","6"]),
    ([GREEN, BLUE, RED], ["1","4","3"]),
    ([RED, GREEN, GREEN], ["3","9","4"]),
    ([GREEN, RED, BLUE], ["1","3","9"]),
]

for i, (dots, nums) in enumerate(rows):
    draw_row(i, dots, nums)

# Save: ensure an 'export' directory exists next to this script
base_dir = Path(__file__).resolve().parent
export_dir = base_dir / "export"
export_dir.mkdir(parents=True, exist_ok=True)
out_path = export_dir / "crack_the_code_exact.png"
img.save(out_path)
print(f"Saved poster to: {out_path}")
