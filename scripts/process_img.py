from PIL import Image, ImageFilter
import os

img = Image.open('C:/Users/ROG/yuchen-website/hero-raw.jpg')
w, h = img.size
print(f"Original size: {w}x{h}")

# --- Step 1: Remove watermark by cropping bottom portion ---
# The watermark "小紅書號：821969991" is at the bottom-right
# Crop bottom ~65px to remove it
crop_bottom = 65
img_cropped = img.crop((0, 0, w, h - crop_bottom))

# --- Step 2: Smart crop for hero use (landscape, 16:9 or wide) ---
# Source is portrait/near-square; crop to wide hero format 1920x900
cw, ch = img_cropped.size
target_ratio = 1920 / 900  # ~2.13

# Crop to target ratio, centered horizontally, favoring top portion for beauty
new_h = int(cw / target_ratio)
if new_h > ch:
    new_w = int(ch * target_ratio)
    left = (cw - new_w) // 2
    hero = img_cropped.crop((left, 0, left + new_w, ch))
else:
    top = int(ch * 0.05)   # slight top crop to cut ceiling
    hero = img_cropped.crop((0, top, cw, top + new_h))

# Resize to 1920x900
hero = hero.resize((1920, 900), Image.LANCZOS)

# Save
out_path = 'C:/Users/ROG/yuchen-website/hero.jpg'
hero.save(out_path, 'JPEG', quality=90, optimize=True)
print(f"Saved hero: {hero.size}, {os.path.getsize(out_path)//1024}KB")

# Also save additional slide images (cropped differently for variety)
# Slide 2: focus on the window/city view (right portion)
cw2, ch2 = img_cropped.size
new_h2 = int(cw2 / target_ratio)
if new_h2 <= ch2:
    top2 = int(ch2 * 0.0)
    slide2 = img_cropped.crop((0, top2, cw2, top2 + new_h2))
else:
    new_w2 = int(ch2 * target_ratio)
    left2 = (cw2 - new_w2) // 2
    slide2 = img_cropped.crop((left2, 0, left2 + new_w2, ch2))
slide2 = slide2.resize((1920, 900), Image.LANCZOS)
slide2.save('C:/Users/ROG/yuchen-website/hero2.jpg', 'JPEG', quality=85)
print("Saved hero2.jpg")
