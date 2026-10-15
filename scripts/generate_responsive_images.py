import os
from PIL import Image

ASSETS_DIR = 'site/assets'

def resize_and_save(src_name, target_name, max_width, quality=82):
    src_path = os.path.join(ASSETS_DIR, src_name)
    target_path = os.path.join(ASSETS_DIR, target_name)
    if not os.path.exists(src_path):
        print(f"Warning: {src_path} does not exist.")
        return
    
    with Image.open(src_path) as im:
        w, h = im.size
        if w <= max_width:
            print(f"{src_name} width ({w}) <= {max_width}, saving copy with quality {quality}...")
            new_w, new_h = w, h
        else:
            ratio = max_width / float(w)
            new_w = max_width
            new_h = int(h * ratio)
            im = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        im.save(target_path, 'WEBP', quality=quality, method=6)
        new_size = os.path.getsize(target_path)
        print(f"Generated {target_name}: {new_w}x{new_h} ({new_size // 1024} KiB)")

# 1. Hero Dog
resize_and_save('hero-dog.webp', 'hero-dog-400.webp', 400, quality=82)
resize_and_save('hero-dog.webp', 'hero-dog-700.webp', 700, quality=82)

# 2. Products Showcase
resize_and_save('products-showcase.webp', 'products-showcase-480.webp', 480, quality=80)
resize_and_save('products-showcase.webp', 'products-showcase-960.webp', 960, quality=82)

# 3. Services
for s in ['vet', 'grooming', 'pharmacy']:
    resize_and_save(f'service-{s}.webp', f'service-{s}-400.webp', 400, quality=80)
    resize_and_save(f'service-{s}.webp', f'service-{s}-700.webp', 700, quality=82)

# 4. Reviews
resize_and_save('review-golden.webp', 'review-golden-280.webp', 280, quality=80)
resize_and_save('review-labrador.webp', 'review-labrador-280.webp', 280, quality=80)

# 5. Mini Products
for i, p in enumerate(['product-1-biscoitos', 'product-2-snacks', 'product-3-kong', 'product-4-dental'], 1):
    resize_and_save(f'{p}.webp', f'{p}-240.webp', 240, quality=80)

print("Responsive image variants generation finished!")
