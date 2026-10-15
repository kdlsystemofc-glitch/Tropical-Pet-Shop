import os
from playwright.sync_api import sync_playwright
from PIL import Image

def generate():
    os.makedirs('site/assets', exist_ok=True)

    # 1. Services orange wave: an organic wave hugging the right edge of section 02
    svg_services = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 800" width="500" height="800">
      <path d="M500,0 C380,60 220,120 200,280 C180,440 340,560 260,700 C220,770 120,790 80,800 L500,800 Z" fill="#FB5F00"/>
      <path d="M500,0 C410,70 280,140 260,300 C240,460 380,570 320,710 C290,770 200,790 160,800 L500,800 Z" fill="#FF6B08" opacity="0.4"/>
    </svg>"""

    # 2. Products orange wave: organic wave emerging at lower right of section 03, transitioning into Avaliações
    svg_products = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 700" width="500" height="700">
      <path d="M500,0 C450,100 480,200 430,320 C370,460 200,500 160,620 C140,680 180,700 200,700 L500,700 Z" fill="#FB5F00"/>
      <path d="M500,0 C470,110 500,210 460,330 C410,470 260,510 220,630 C200,685 230,700 250,700 L500,700 Z" fill="#FF6B08" opacity="0.4"/>
    </svg>"""

    temp_s = os.path.abspath('temp_s.html')
    temp_p = os.path.abspath('temp_p.html')

    with open(temp_s, 'w', encoding='utf-8') as f:
        f.write(f'<!DOCTYPE html><html><body style="margin:0;background:transparent;overflow:hidden;">{svg_services}</body></html>')

    with open(temp_p, 'w', encoding='utf-8') as f:
        f.write(f'<!DOCTYPE html><html><body style="margin:0;background:transparent;overflow:hidden;">{svg_products}</body></html>')

    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # Render services wave
        page = browser.new_page(viewport={'width': 500, 'height': 800})
        page.goto(f'file:///{temp_s}')
        page.screenshot(path='site/assets/services-orange-wave.png', omit_background=True)
        page.close()
        
        # Render products wave
        page2 = browser.new_page(viewport={'width': 500, 'height': 700})
        page2.goto(f'file:///{temp_p}')
        page2.screenshot(path='site/assets/products-orange-wave.png', omit_background=True)
        page2.close()
        
        browser.close()

    # Convert to WebP
    Image.open('site/assets/services-orange-wave.png').save('site/assets/services-orange-wave.webp', 'WEBP', quality=95)
    Image.open('site/assets/products-orange-wave.png').save('site/assets/products-orange-wave.webp', 'WEBP', quality=95)

    # Clean up temps
    if os.path.exists(temp_s): os.remove(temp_s)
    if os.path.exists(temp_p): os.remove(temp_p)
    if os.path.exists('site/assets/services-orange-wave.png'): os.remove('site/assets/services-orange-wave.png')
    if os.path.exists('site/assets/products-orange-wave.png'): os.remove('site/assets/products-orange-wave.png')

    print('Wave generation completed successfully!')

if __name__ == '__main__':
    generate()
