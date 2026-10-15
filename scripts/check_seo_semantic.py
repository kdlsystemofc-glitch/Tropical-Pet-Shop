import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=== HEADINGS HIERARCHY ===")
headings = re.findall(r'<h([1-6])[^>]*>([\s\S]*?)</h\1>', html)
for level, text in headings:
    clean_text = re.sub(r'<[^>]+>', ' ', text)
    clean_text = ' '.join(clean_text.split())
    # remove emojis that might fail in windows console cp1252
    clean_ascii = clean_text.encode('ascii', 'replace').decode('ascii')
    print(f"H{level}: {clean_ascii}")

print("\n=== IMAGES AUDIT ===")
images = re.findall(r'<img([^>]+)>', html)
for i, attrs in enumerate(images, 1):
    src = re.search(r'src="([^"]+)"', attrs)
    alt = re.search(r'alt="([^"]*)"', attrs)
    role = re.search(r'role="([^"]+)"', attrs)
    aria_hidden = re.search(r'aria-hidden="([^"]+)"', attrs)
    
    src_val = src.group(1) if src else 'N/A'
    alt_val = alt.group(1) if alt else '[MISSING ALT]'
    print(f"{i}. src: {src_val}")
    print(f"   alt: '{alt_val}'")
