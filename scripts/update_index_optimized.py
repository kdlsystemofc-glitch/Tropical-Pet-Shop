import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('site/css/critical.min.css', 'r', encoding='utf-8') as f:
    critical_css = f.read()

# 1. Update <head>
new_head_content = f"""  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐾</text></svg>">
  <!-- Preload local WOFF2 critical fonts -->
  <link rel="preload" href="site/fonts/plus-jakarta-sans-800-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="site/fonts/dm-sans-400-latin.woff2" as="font" type="font/woff2" crossorigin>
  <!-- Inline Critical CSS -->
  <style id="critical-css">{critical_css}</style>
  <!-- Asynchronous Non-Critical CSS (Print onload trick recommended by web.dev) -->
  <link rel="stylesheet" href="site/css/style.min.css" media="print" onload="this.media='all'">
  <noscript><link rel="stylesheet" href="site/css/style.min.css"></noscript>"""

old_head_pattern = r'  <link rel="icon" href="data:image/svg\+xml,[^"]+">\s*<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*<link rel="stylesheet" href="site/css/tokens\.css">\s*<link rel="stylesheet" href="site/css/reset\.css">\s*<link rel="stylesheet" href="site/css/style\.css">'

if re.search(old_head_pattern, html):
    html = re.sub(old_head_pattern, new_head_content, html)
    print("Updated <head> with critical CSS and preloaded fonts.")
else:
    print("Warning: old_head_pattern did not match directly, performing fallback replacement.")
    # Fallback replacement
    start_tag = '<meta name="description" content="Pet shop completo em São Bernardo do Campo: Clínica Veterinária com a Dra. Vânia, Banho e Tosa, Farmácia e Rações Super Premium com entrega rápida via WhatsApp.">'
    end_tag = '</head>'
    head_sub = f"{start_tag}\n{new_head_content}\n"
    html = html.replace(html[html.find(start_tag):html.find(end_tag)], head_sub)

# 2. Hero Dog responsive image
old_hero_dog = '<img src="site/assets/hero-dog.webp" alt="Cãozinho Jack Russell saltando alegremente com brinquedo" class="hero-dog-jumping" width="600" height="600" loading="eager" fetchpriority="high">'
new_hero_dog = """<img src="site/assets/hero-dog.webp"
               srcset="site/assets/hero-dog-400.webp 400w, site/assets/hero-dog-700.webp 700w, site/assets/hero-dog.webp 1122w"
               sizes="(max-width: 600px) 280px, (max-width: 1024px) 450px, 600px"
               alt="Cãozinho Jack Russell saltando alegremente com brinquedo"
               class="hero-dog-jumping"
               width="600" height="750"
               loading="eager" fetchpriority="high">"""
if old_hero_dog in html:
    html = html.replace(old_hero_dog, new_hero_dog)
    print("Updated hero dog responsive image.")

# 3. Products Showcase responsive image
old_showcase = '<img src="site/assets/products-showcase.webp" alt="Linha completa de rações super premium, petiscos e brinquedos" class="showcase-hero-img" width="2172" height="724" loading="lazy">'
new_showcase = """<img src="site/assets/products-showcase.webp"
                 srcset="site/assets/products-showcase-480.webp 480w, site/assets/products-showcase-960.webp 960w, site/assets/products-showcase.webp 2172w"
                 sizes="(max-width: 768px) 95vw, (max-width: 1200px) 55vw, 680px"
                 alt="Linha completa de rações super premium, petiscos e brinquedos"
                 class="showcase-hero-img"
                 width="2172" height="724"
                 loading="lazy">"""
if old_showcase in html:
    html = html.replace(old_showcase, new_showcase)
    print("Updated products showcase responsive image.")

# 4. Service cards responsive images
for s, alt in [('vet', 'Veterinária atenciosa com filhote caramelo'),
               ('grooming', 'Cão feliz tomando banho com espuma perfumada'),
               ('pharmacy', 'Gatinho ruivo na farmácia veterinária com remédios')]:
    old_card = f'<img src="site/assets/service-{s}.webp" alt="{alt}" class="service-card-img" width="1254" height="1254" loading="lazy">'
    new_card = f"""<img src="site/assets/service-{s}.webp"
                    srcset="site/assets/service-{s}-400.webp 400w, site/assets/service-{s}-700.webp 700w, site/assets/service-{s}.webp 1254w"
                    sizes="(max-width: 820px) 92vw, 380px"
                    alt="{alt}"
                    class="service-card-img"
                    width="1254" height="1254"
                    loading="lazy">"""
    if old_card in html:
        html = html.replace(old_card, new_card)
        print(f"Updated service-{s} responsive image.")

# 5. Reviews photos responsive images
old_golden = '<img src="site/assets/review-golden.webp" alt="Golden Retriever sorridente" class="pet-golden-img" width="1254" height="1254" loading="lazy">'
new_golden = """<img src="site/assets/review-golden.webp"
                srcset="site/assets/review-golden-280.webp 280w, site/assets/review-golden.webp 1254w"
                sizes="(max-width: 860px) 140px, 160px"
                alt="Golden Retriever sorridente"
                class="pet-golden-img"
                width="1254" height="1254"
                loading="lazy">"""
if old_golden in html:
    html = html.replace(old_golden, new_golden)
    print("Updated review golden responsive image.")

old_labrador = '<img src="site/assets/review-labrador.webp" alt="Labrador Retriever amarelo feliz na grama" class="pet-labrador-img" width="1024" height="1024" loading="lazy">'
new_labrador = """<img src="site/assets/review-labrador.webp"
                  srcset="site/assets/review-labrador-280.webp 280w, site/assets/review-labrador.webp 1024w"
                  sizes="(max-width: 860px) 140px, 160px"
                  alt="Labrador Retriever amarelo feliz na grama"
                  class="pet-labrador-img"
                  width="1024" height="1024"
                  loading="lazy">"""
if old_labrador in html:
    html = html.replace(old_labrador, new_labrador)
    print("Updated review labrador responsive image.")

# 6. Mini Products responsive images
mini_map = [
    ('product-1-biscoitos', 'Biscoitos e petiscos crocantes para cães'),
    ('product-2-snacks', 'Snacks naturais e nutritivos'),
    ('product-3-kong', 'Brinquedos resistentes e mordedores'),
    ('product-4-dental', 'Itens de higiene oral e dental canina')
]
for p, alt in mini_map:
    old_p = f'<img src="site/assets/{p}.webp" alt="{alt}" class="product-mini-img" width="420" height="420" loading="lazy">'
    new_p = f"""<img src="site/assets/{p}.webp"
                 srcset="site/assets/{p}-240.webp 240w, site/assets/{p}.webp 420w"
                 sizes="(max-width: 768px) 45vw, 150px"
                 alt="{alt}"
                 class="product-mini-img"
                 width="420" height="420"
                 loading="lazy">"""
    if old_p in html:
        html = html.replace(old_p, new_p)
        print(f"Updated {p} responsive image.")

# 7. Use minified scripts
html = html.replace('site/js/motion-core.js', 'site/js/motion-core.min.js')
html = html.replace('site/js/motion-sections.js', 'site/js/motion-sections.min.js')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated with all optimizations!")
