import os
from PIL import Image, ImageDraw

def draw_paw(draw, cx, cy, size, fill_color):
    """Draws a clean, proportioned pet paw icon centered at (cx, cy)."""
    # Main pad (center)
    mp_w = size * 0.55
    mp_h = size * 0.44
    mp_y = cy + size * 0.08
    # Center pad is an oval with soft top
    draw.ellipse([cx - mp_w/2, mp_y - mp_h/2, cx + mp_w/2, mp_y + mp_h/2], fill=fill_color)
    
    # 4 Toe pads
    toe_r_x = size * 0.13
    toe_r_y = size * 0.17
    
    # Toe 1 (far left)
    t1_x = cx - size * 0.32
    t1_y = cy - size * 0.12
    draw.ellipse([t1_x - toe_r_x, t1_y - toe_r_y, t1_x + toe_r_x, t1_y + toe_r_y], fill=fill_color)
    
    # Toe 2 (mid left)
    t2_x = cx - size * 0.12
    t2_y = cy - size * 0.28
    draw.ellipse([t2_x - toe_r_x, t2_y - toe_r_y, t2_x + toe_r_x, t2_y + toe_r_y], fill=fill_color)
    
    # Toe 3 (mid right)
    t3_x = cx + size * 0.12
    t3_y = cy - size * 0.28
    draw.ellipse([t3_x - toe_r_x, t3_y - toe_r_y, t3_x + toe_r_x, t3_y + toe_r_y], fill=fill_color)
    
    # Toe 4 (far right)
    t4_x = cx + size * 0.32
    t4_y = cy - size * 0.12
    draw.ellipse([t4_x - toe_r_x, t4_y - toe_r_y, t4_x + toe_r_x, t4_y + toe_r_y], fill=fill_color)

def generate_icon(size, is_rounded_rect=False):
    # Render at 4x for clean antialiasing
    scale = 4
    canvas_size = size * scale
    img = Image.new('RGBA', (canvas_size, canvas_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background: Tropical Orange (#FF6000)
    bg_color = (255, 96, 0, 255)
    margin = int(canvas_size * 0.05)
    
    if is_rounded_rect:
        radius = int(canvas_size * 0.22)
        draw.rounded_rectangle([margin, margin, canvas_size - margin, canvas_size - margin], radius=radius, fill=bg_color)
    else:
        draw.ellipse([margin, margin, canvas_size - margin, canvas_size - margin], fill=bg_color)
        
    # Draw Paw in Pure White (#FFFFFF)
    draw_paw(draw, canvas_size / 2, canvas_size / 2 + canvas_size * 0.02, canvas_size * 0.62, (255, 255, 255, 255))
    
    # Downsample with Lanczos
    return img.resize((size, size), Image.Resampling.LANCZOS)

sizes = {
    'site/assets/favicon-16x16.png': (16, False),
    'site/assets/favicon-32x32.png': (32, False),
    'site/assets/apple-touch-icon.png': (180, True),
    'site/assets/favicon-192.png': (192, True),
    'site/assets/favicon-512.png': (512, True),
}

for path, (s, is_rounded) in sizes.items():
    icon = generate_icon(s, is_rounded_rect=is_rounded)
    icon.save(path, 'PNG')
    print(f"Generated {path} ({s}x{s})")

# Generate standard favicon.ico
ico_img = generate_icon(48, False)
ico_img.save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
ico_img.save('site/assets/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
print("Generated favicon.ico (16, 32, 48px)")
