import os
import re

def minify_css(css):
    # Remove comments
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    # Normalize whitespace
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', css)
    css = re.sub(r';\}', '}', css)
    return css.strip()

# Read fonts.css, tokens.css, reset.css, style.css
with open('site/fonts/fonts.css', 'r', encoding='utf-8') as f:
    fonts_css = f.read()

with open('site/css/tokens.css', 'r', encoding='utf-8') as f:
    tokens_css = f.read()
    # Remove remote @import if any
    tokens_css = re.sub(r'@import\s+url\([^)]+\);', '', tokens_css)

with open('site/css/reset.css', 'r', encoding='utf-8') as f:
    reset_css = f.read()

with open('site/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

# Split style.css at .section-products so Header + Hero + Serviços are in Critical CSS
hero_part, rest_part = style_css.split('.section-products', 1)
rest_part = '.section-products' + rest_part

# Baseline rules for decorative blob wrappers to prevent any CLS before non-critical CSS loads
blob_baseline = """
.services-blob-wrapper, .products-blob-wrapper, .reviews-blob-wrapper {
  position: absolute;
  pointer-events: none;
}
"""

critical_combined = f"{fonts_css}\n{tokens_css}\n{reset_css}\n{blob_baseline}\n{hero_part}"
# Adjust relative paths for inline CSS inside index.html located at project root
critical_combined = critical_combined.replace('../fonts/', 'site/fonts/').replace('../assets/', 'site/assets/')
critical_min = minify_css(critical_combined)

with open('site/css/critical.min.css', 'w', encoding='utf-8') as f:
    f.write(critical_min)

non_critical_combined = rest_part
non_critical_min = minify_css(non_critical_combined)

with open('site/css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(non_critical_min)

print(f"Critical CSS size: {len(critical_min.encode('utf-8')) / 1024:.1f} KiB")
print(f"Non-critical CSS size: {len(non_critical_min.encode('utf-8')) / 1024:.1f} KiB")
