import os
from PIL import Image, ImageDraw, ImageFont

def create_og_image():
    W, H = 1200, 630
    # 1. Base canvas with brand warm background (#FAF6F0)
    bg_color = (250, 246, 240)
    canvas = Image.new('RGB', (W, H), bg_color)
    
    # 2. Add organic peach and orange shapes in background
    blob_overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    blob_draw = ImageDraw.Draw(blob_overlay)
    
    # Large soft peach blob on right
    blob_draw.ellipse([650, -80, 1350, 680], fill=(255, 211, 180, 220))
    # Intense tropical orange blob (#FF6000)
    blob_draw.ellipse([760, 60, 1300, 600], fill=(255, 96, 0, 230))
    
    # Merge blobs onto canvas
    canvas.paste(blob_overlay, (0, 0), blob_overlay)
    
    # 3. Paste Hero Dog on right
    dog_path = 'site/assets/hero-dog.webp'
    if os.path.exists(dog_path):
        dog = Image.open(dog_path).convert('RGBA')
        # Target dog height ~ 500px
        dog_h = 510
        dog_w = int(dog.width * (dog_h / dog.height))
        dog_resized = dog.resize((dog_w, dog_h), Image.Resampling.LANCZOS)
        
        # Position dog jumping towards left-center
        dog_x = W - dog_w - 40
        dog_y = (H - dog_h) // 2 + 30
        canvas.paste(dog_resized, (dog_x, dog_y), dog_resized)
        
    # 4. Text and Branding on Left Side
    draw = ImageDraw.Draw(canvas)
    
    # Fonts
    font_badge = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 20)
    font_h1 = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 64)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 26)
    font_body = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 22)
    font_bold = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 23)

    margin_left = 75
    
    # Top Tag / Pill Badge: "28 ANOS DE TRADIÇÃO EM SBC"
    badge_text = "28 ANOS DE TRADIÇÃO EM SÃO BERNARDO DO CAMPO"
    badge_bg = (255, 231, 214) # Peach soft
    badge_color = (200, 76, 0) # Accessible dark orange
    
    # Draw pill
    pill_x, pill_y = margin_left, 70
    bbox = draw.textbbox((pill_x, pill_y), badge_text, font=font_badge)
    draw.rounded_rectangle(
        [pill_x - 16, pill_y - 6, bbox[2] + 16, bbox[3] + 8],
        radius=20,
        fill=badge_bg,
        outline=(255, 175, 120),
        width=1
    )
    draw.text((pill_x, pill_y), badge_text, font=font_badge, fill=badge_color)
    
    # Main Title: TROPICAL PET SHOP
    title_y = pill_y + 55
    draw.text((margin_left, title_y), "TROPICAL PET SHOP", font=font_h1, fill=(44, 24, 16))
    
    # Accent Line underneath
    draw.rectangle([margin_left, title_y + 80, margin_left + 120, title_y + 86], fill=(255, 96, 0))
    
    # Services Subhead
    subhead_y = title_y + 105
    draw.text((margin_left, subhead_y), "Clínica Veterinária • Banho & Tosa • Rações Super Premium", font=font_sub, fill=(230, 85, 0))
    
    # Description
    desc_y = subhead_y + 48
    draw.text((margin_left, desc_y), "Atendimento com a Dra. Vânia, estética animal carinhosa\ne linha completa de nutrição e farmácia veterinária.", font=font_body, fill=(90, 67, 53))
    
    # Info Box Card
    card_y = desc_y + 80
    card_w = 600
    card_h = 135
    draw.rounded_rectangle(
        [margin_left, card_y, margin_left + card_w, card_y + card_h],
        radius=18,
        fill=(255, 255, 255),
        outline=(240, 228, 215),
        width=2
    )
    
    # Card Contents
    draw.text((margin_left + 24, card_y + 24), "Endereço: Rua Espanha, 415 — Vila Santa Luzia, SBC", font=font_body, fill=(60, 40, 30))
    draw.text((margin_left + 24, card_y + 70), "Pedidos e Agendamentos via WhatsApp: (11) 96036-5965", font=font_bold, fill=(200, 76, 0))
    
    # 5. Save as high quality JPG and WebP
    out_jpg = 'site/assets/og-image.jpg'
    out_webp = 'site/assets/og-image.webp'
    canvas.save(out_jpg, 'JPEG', quality=90, optimize=True)
    canvas.save(out_webp, 'WEBP', quality=88)
    
    print(f"Generated {out_jpg} ({W}x{H}, {os.path.getsize(out_jpg)/1024:.1f} KiB)")
    print(f"Generated {out_webp} ({W}x{H}, {os.path.getsize(out_webp)/1024:.1f} KiB)")

if __name__ == '__main__':
    create_og_image()
