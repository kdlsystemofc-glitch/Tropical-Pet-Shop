import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update src to mobile-first variants
replacements = [
    ('src="site/assets/hero-dog.webp"', 'src="site/assets/hero-dog-400.webp"'),
    ('src="site/assets/hero-orange-blob.webp"', 'src="site/assets/hero-orange-blob-480.webp"'),
    ('src="site/assets/service-vet.webp"', 'src="site/assets/service-vet-360.webp"'),
    ('src="site/assets/service-grooming.webp"', 'src="site/assets/service-grooming-360.webp"'),
    ('src="site/assets/service-pharmacy.webp"', 'src="site/assets/service-pharmacy-360.webp"'),
    ('src="site/assets/products-showcase.webp"', 'src="site/assets/products-showcase-360.webp"'),
    ('src="site/assets/product-1-biscoitos.webp"', 'src="site/assets/product-1-biscoitos-160.webp"'),
    ('src="site/assets/product-2-snacks.webp"', 'src="site/assets/product-2-snacks-160.webp"'),
    ('src="site/assets/product-3-kong.webp"', 'src="site/assets/product-3-kong-160.webp"'),
    ('src="site/assets/product-4-dental.webp"', 'src="site/assets/product-4-dental-160.webp"'),
    ('src="site/assets/reviews-orange-blob.webp"', 'src="site/assets/reviews-orange-blob-600.webp"'),
    ('src="site/assets/review-golden.webp"', 'src="site/assets/review-golden-280.webp"'),
    ('src="site/assets/review-labrador.webp"', 'src="site/assets/review-labrador-280.webp"'),
]

for old, new in replacements:
    html = html.replace(old, new)

# 2. Update motion script loader to load on interaction or 3.5s idle
old_loader_pattern = r'<script>\s*\(function \(\) \{[\s\S]*?loadMotionScripts[\s\S]*?\}\)\(\);\s*</script>'
new_loader = """<script>
    (function () {
      var loaded = false;
      function loadMotionScripts() {
        if (loaded) return;
        loaded = true;
        var scripts = [
          'site/js/vendor/gsap.min.js',
          'site/js/vendor/ScrollTrigger.min.js',
          'site/js/vendor/lenis.min.js',
          'site/js/motion-core.min.js',
          'site/js/motion-sections.min.js'
        ];
        function next(idx) {
          if (idx >= scripts.length) return;
          var s = document.createElement('script');
          s.src = scripts[idx];
          s.onload = function () { next(idx + 1); };
          document.body.appendChild(s);
        }
        next(0);
      }
      // Carrega na primeira interação do usuário ou após 3.5s de inatividade
      ['scroll', 'touchstart', 'mousemove', 'keydown', 'click'].forEach(function (ev) {
        window.addEventListener(ev, loadMotionScripts, { once: true, passive: true });
      });
      setTimeout(loadMotionScripts, 3500);
    })();
  </script>"""

html = re.sub(old_loader_pattern, new_loader, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with mobile-first src and interaction/idle script loader!")
