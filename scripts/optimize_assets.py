import os
from PIL import Image

def resize_webp(src_path, dst_path, target_width, quality=82):
    if not os.path.exists(src_path):
        print(f"Skipping {src_path}, does not exist")
        return
    img = Image.open(src_path)
    w_orig, h_orig = img.size
    if target_width >= w_orig:
        target_width = w_orig
    target_height = int(round(h_orig * (target_width / float(w_orig))))
    resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    resized.save(dst_path, 'WEBP', quality=quality, method=6)
    kb = os.path.getsize(dst_path) / 1024
    print(f"Generated {dst_path}: {target_width}x{target_height} ({kb:.1f} KiB)")

# 1. Hero Dog
resize_webp('site/assets/hero-dog.webp', 'site/assets/hero-dog-400.webp', 400, quality=78)
resize_webp('site/assets/hero-dog.webp', 'site/assets/hero-dog-600.webp', 600, quality=78)
resize_webp('site/assets/hero-dog.webp', 'site/assets/hero-dog-720.webp', 720, quality=78)

# 2. Hero Orange Blob
resize_webp('site/assets/hero-orange-blob.webp', 'site/assets/hero-orange-blob-480.webp', 480, quality=80)
resize_webp('site/assets/hero-orange-blob.webp', 'site/assets/hero-orange-blob-800.webp', 800, quality=80)

# 3. Reviews Orange Blob
resize_webp('site/assets/reviews-orange-blob.webp', 'site/assets/reviews-orange-blob-600.webp', 600, quality=80)

# 4. Services Cards
for s in ['vet', 'grooming', 'pharmacy']:
    resize_webp(f'site/assets/service-{s}.webp', f'site/assets/service-{s}-360.webp', 360, quality=78)
    resize_webp(f'site/assets/service-{s}.webp', f'site/assets/service-{s}-600.webp', 600, quality=78)
    resize_webp(f'site/assets/service-{s}.webp', f'site/assets/service-{s}-800.webp', 800, quality=78)

# 5. Products Showcase
resize_webp('site/assets/products-showcase.webp', 'site/assets/products-showcase-360.webp', 360, quality=78)
resize_webp('site/assets/products-showcase.webp', 'site/assets/products-showcase-680.webp', 680, quality=78)
resize_webp('site/assets/products-showcase.webp', 'site/assets/products-showcase-1000.webp', 1000, quality=78)

# 6. Mini Products
for i, p in enumerate(['product-1-biscoitos', 'product-2-snacks', 'product-3-kong', 'product-4-dental'], 1):
    resize_webp(f'site/assets/{p}.webp', f'site/assets/{p}-160.webp', 160, quality=78)
    resize_webp(f'site/assets/{p}.webp', f'site/assets/{p}-240.webp', 240, quality=78)
    resize_webp(f'site/assets/{p}.webp', f'site/assets/{p}-300.webp', 300, quality=78)

print("All optimized assets generated successfully!")
