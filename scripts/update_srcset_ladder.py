import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update <head> preload
old_preload = re.search(r'<link rel="preload" as="image"[^>]+>', html)
new_preload = '<link rel="preload" as="image" href="site/assets/hero-dog-600.webp" imagesrcset="site/assets/hero-dog-400.webp 400w, site/assets/hero-dog-600.webp 600w, site/assets/hero-dog-720.webp 720w, site/assets/hero-dog.webp 1122w" imagesizes="(max-width: 600px) 260px, (max-width: 1024px) 340px, 420px" fetchpriority="high">'
if old_preload:
    html = html.replace(old_preload.group(0), new_preload)

# 2. Hero Dog Jumping
hero_dog_pattern = r'<img src="site/assets/hero-dog-400\.webp"[\s\S]*?class="hero-dog-jumping"[\s\S]*?>'
new_hero_dog = """<img src="site/assets/hero-dog-400.webp"
               srcset="site/assets/hero-dog-400.webp 400w, site/assets/hero-dog-600.webp 600w, site/assets/hero-dog-720.webp 720w, site/assets/hero-dog.webp 1122w"
               sizes="(max-width: 600px) 260px, (max-width: 1024px) 340px, 420px"
               alt="Cãozinho Jack Russell saltando alegremente com brinquedo"
               class="hero-dog-jumping"
               width="600" height="750"
               loading="eager" fetchpriority="high">"""
html = re.sub(hero_dog_pattern, new_hero_dog, html)

# 3. Service Cards
for s, alt in [('vet', 'Veterinária atenciosa com filhote caramelo'),
               ('grooming', 'Cão feliz tomando banho com espuma perfumada'),
               ('pharmacy', 'Gatinho ruivo na farmácia veterinária com remédios')]:
    card_pattern = rf'<img src="site/assets/service-{s}-360\.webp"[\s\S]*?class="service-card-img"[\s\S]*?>'
    new_card = f"""<img src="site/assets/service-{s}-360.webp"
                    srcset="site/assets/service-{s}-360.webp 360w, site/assets/service-{s}-600.webp 600w, site/assets/service-{s}-800.webp 800w, site/assets/service-{s}.webp 1254w"
                    sizes="(max-width: 820px) 92vw, 380px"
                    alt="{alt}"
                    class="service-card-img"
                    width="1254" height="1254"
                    loading="lazy">"""
    html = re.sub(card_pattern, new_card, html)

# 4. Products Showcase
showcase_pattern = r'<img src="site/assets/products-showcase-360\.webp"[\s\S]*?class="showcase-hero-img"[\s\S]*?>'
new_showcase = """<img src="site/assets/products-showcase-360.webp"
                 srcset="site/assets/products-showcase-360.webp 360w, site/assets/products-showcase-680.webp 680w, site/assets/products-showcase-1000.webp 1000w, site/assets/products-showcase.webp 2172w"
                 sizes="(max-width: 768px) 95vw, 680px"
                 alt="Linha completa de rações super premium, petiscos e brinquedos"
                 class="showcase-hero-img"
                 width="2172" height="724"
                 loading="lazy">"""
html = re.sub(showcase_pattern, new_showcase, html)

# 5. Mini Products
mini_map = [
    ('product-1-biscoitos', 'Biscoitos e petiscos crocantes para cães'),
    ('product-2-snacks', 'Snacks naturais e bifinhos mastigáveis'),
    ('product-3-kong', 'Brinquedos interativos Kong e mordedores'),
    ('product-4-dental', 'Anel dental e produtos para higiene oral pet')
]
for p, alt in mini_map:
    p_pattern = rf'<img src="site/assets/{p}-160\.webp"[\s\S]*?class="product-mini-img"[\s\S]*?>'
    new_p = f"""<img src="site/assets/{p}-160.webp"
                 srcset="site/assets/{p}-160.webp 160w, site/assets/{p}-240.webp 240w, site/assets/{p}-300.webp 300w, site/assets/{p}.webp 420w"
                 sizes="(max-width: 768px) 140px, 150px"
                 alt="{alt}"
                 class="product-mini-img"
                 width="420" height="420"
                 loading="lazy">"""
    html = re.sub(p_pattern, new_p, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated with high-DPR srcset ladders!")
