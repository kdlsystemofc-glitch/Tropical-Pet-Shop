import os
import re
import urllib.request

FONTS_DIR = 'site/fonts'
os.makedirs(FONTS_DIR, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = 'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Plus+Jakarta+Sans:wght@700;800;900&display=swap'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    css = resp.read().decode('utf-8')

blocks = re.findall(r'/\* ([^*]+) \*/\s*@font-face\s*\{([^}]+)\}', css)

local_css_rules = []
for subset, rule in blocks:
    subset = subset.strip()
    if subset not in ['latin', 'latin-ext']:
        continue
    
    font_family_match = re.search(r"font-family:\s*['\"]([^'\"]+)['\"]", rule)
    font_weight_match = re.search(r"font-weight:\s*(\d+)", rule)
    font_style_match = re.search(r"font-style:\s*(\w+)", rule)
    src_match = re.search(r"src:\s*url\((https://[^)]+\.woff2)\)", rule)
    unicode_match = re.search(r"unicode-range:\s*([^;]+);", rule)

    if not (font_family_match and font_weight_match and src_match):
        continue

    family = font_family_match.group(1)
    weight = font_weight_match.group(1)
    style = font_style_match.group(1) if font_style_match else 'normal'
    src_url = src_match.group(1)
    unicode_range = unicode_match.group(1) if unicode_match else None

    safe_family = family.lower().replace(' ', '-')
    filename = f"{safe_family}-{weight}-{subset}.woff2"
    filepath = os.path.join(FONTS_DIR, filename)

    if not os.path.exists(filepath):
        print(f"Downloading {filename} from {src_url}...")
        file_req = urllib.request.Request(src_url, headers=headers)
        with urllib.request.urlopen(file_req) as f_resp:
            with open(filepath, 'wb') as out_f:
                out_f.write(f_resp.read())
    else:
        print(f"File {filename} already exists.")

    rule_str = f"""/* {subset} */
@font-face {{
  font-family: '{family}';
  font-style: {style};
  font-weight: {weight};
  font-display: swap;
  src: url('../fonts/{filename}') format('woff2');"""
    if unicode_range:
        rule_str += f"\n  unicode-range: {unicode_range};"
    rule_str += "\n}\n"
    local_css_rules.append(rule_str)

css_output_path = os.path.join(FONTS_DIR, 'fonts.css')
with open(css_output_path, 'w', encoding='utf-8') as f:
    f.write('/* Local WOFF2 Google Fonts for Tropical Pet Shop (DM Sans + Plus Jakarta Sans) */\n\n')
    f.write('\n'.join(local_css_rules))

print(f"Generated {css_output_path} with {len(local_css_rules)} font faces.")
