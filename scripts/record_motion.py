import os
import time
import shutil
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

PORT = 8765
SERVER_STARTED = False

def start_server():
    global SERVER_STARTED
    if not SERVER_STARTED:
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(root_dir)
        server = HTTPServer(('127.0.0.1', PORT), SimpleHTTPRequestHandler)
        t = threading.Thread(target=server.serve_forever, daemon=True)
        t.start()
        SERVER_STARTED = True
        time.sleep(0.5)

def record():
    start_server()
    os.makedirs('screenshots/video', exist_ok=True)
    temp_video_dir = os.path.abspath('screenshots/video/temp')
    os.makedirs(temp_video_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1440, 'height': 900},
            record_video_dir=temp_video_dir,
            record_video_size={'width': 1440, 'height': 900}
        )
        page = context.new_page()

        print("Navigating to page...")
        page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until='networkidle')
        page.evaluate("document.fonts.ready")
        
        # 1. Hero observation
        print("Observing Hero entrance and loops...")
        time.sleep(2.0)

        # 2. Scroll to Serviços
        print("Scrolling to Serviços...")
        page.locator("#servicos").scroll_into_view_if_needed()
        time.sleep(1.8)

        # 3. Scroll to Produtos
        print("Scrolling to Produtos...")
        page.locator("#produtos").scroll_into_view_if_needed()
        time.sleep(1.8)

        # 4. Scroll to Avaliações
        print("Scrolling to Avaliações...")
        page.locator("#avaliacoes").scroll_into_view_if_needed()
        time.sleep(2.0)

        # 5. Scroll to Rodapé
        print("Scrolling to Rodapé...")
        page.locator("#cta-footer").scroll_into_view_if_needed()
        time.sleep(2.0)

        # 6. Test Pause Toggle Button
        print("Testing Motion Pause Button...")
        pause_btn = page.locator("#motion-toggle-btn")
        if pause_btn.count() > 0:
            pause_btn.click()
            time.sleep(1.2)
            pause_btn.click()
            time.sleep(1.0)

        # 7. Scroll back to top
        print("Scrolling back to top...")
        page.locator("#hero").scroll_into_view_if_needed()
        time.sleep(1.5)

        page.close()
        video_path = page.video.path() if page.video else None
        context.close()
        browser.close()

        if video_path and os.path.exists(video_path):
            final_path = os.path.abspath('screenshots/video/motion_walkthrough.webm')
            shutil.copy(video_path, final_path)
            shutil.rmtree(temp_video_dir, ignore_errors=True)
            print(f"Motion video saved successfully: {final_path}")
            return final_path
        else:
            print("Failed to record video file.")
            return None

if __name__ == '__main__':
    record()
