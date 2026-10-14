import argparse
import os
import sys
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from playwright.sync_api import sync_playwright

PORT = 8765
SERVER_STARTED = False

def start_server():
    global SERVER_STARTED
    if not SERVER_STARTED:
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        server = HTTPServer(('127.0.0.1', PORT), SimpleHTTPRequestHandler)
        t = threading.Thread(target=server.serve_forever, daemon=True)
        t.start()
        SERVER_STARTED = True
        time.sleep(0.5)

def capture(section=None, prev_section=None, viewports=None, prefix=""):
    start_server()
    if viewports is None:
        viewports = [(1440, 900), (390, 844)]
    
    os.makedirs('screenshots', exist_ok=True)
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for w, h in viewports:
            context = browser.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2)
            page = context.new_page()
            url = f"http://127.0.0.1:{PORT}/index.html"
            page.goto(url, wait_until='networkidle')
            page.evaluate("document.fonts.ready")
            time.sleep(0.5) # ensure styles and images render

            vp_tag = f"{w}"
            
            # 1. Full page
            fp_name = f"screenshots/{prefix}fullpage-{section or 'all'}-{vp_tag}.png"
            page.screenshot(path=fp_name, full_page=True)
            results.append(fp_name)
            print(f"Captured full page: {fp_name}")

            # 2. Section isolated
            if section:
                locator = page.locator(f"#{section}")
                if locator.count() > 0:
                    sec_name = f"screenshots/{prefix}section-{section}-{vp_tag}.png"
                    locator.screenshot(path=sec_name)
                    results.append(sec_name)
                    print(f"Captured section {section}: {sec_name}")
                else:
                    print(f"Warning: Section #{section} not found!")

            # 3. Seam / Costura with previous section
            if prev_section and section:
                prev_loc = page.locator(f"#{prev_section}")
                curr_loc = page.locator(f"#{section}")
                if prev_loc.count() > 0 and curr_loc.count() > 0:
                    prev_box = prev_loc.bounding_box()
                    curr_box = curr_loc.bounding_box()
                    if prev_box and curr_box:
                        # Capture transition region: bottom 250px of prev and top 250px of curr
                        top_y = max(0, prev_box['y'] + prev_box['height'] - 250)
                        bottom_y = curr_box['y'] + min(250, curr_box['height'])
                        seam_h = max(100, bottom_y - top_y)
                        seam_name = f"screenshots/{prefix}costura-{prev_section}-{section}-{vp_tag}.png"
                        page.screenshot(path=seam_name, clip={'x': 0, 'y': top_y, 'width': w, 'height': seam_h})
                        results.append(seam_name)
                        print(f"Captured seam {prev_section} -> {section}: {seam_name}")

            context.close()
        browser.close()
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--section', type=str, default=None)
    parser.add_argument('--prev-section', type=str, default=None)
    parser.add_argument('--all-viewports', action='store_true')
    parser.add_argument('--prefix', type=str, default="")
    args = parser.parse_args()

    vps = [(1440, 900), (768, 1024), (390, 844)] if args.all_viewports else [(1440, 900), (390, 844)]
    capture(section=args.section, prev_section=args.prev_section, viewports=vps, prefix=args.prefix)
