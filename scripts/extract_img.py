import json, base64, re

with open('C:/Users/ROG/.claude/projects/C--Users-ROG/3ef12dab-c40c-4837-89f5-0c20f35a710d.jsonl', 'r', encoding='utf-8') as f:
    content = f.read()

# Find image base64 data
idx = content.find('"type":"image"')
if idx >= 0:
    data_start = content.find('"data":"', idx) + 8
    data_end = content.find('"', data_start)
    b64data = content[data_start:data_end]
    img_bytes = base64.b64decode(b64data)
    with open('C:/Users/ROG/yuchen-website/hero-raw.jpg', 'wb') as f:
        f.write(img_bytes)
    print(f'Saved raw image: {len(img_bytes)} bytes')
else:
    print('Image not found')
