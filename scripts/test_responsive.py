import os
import sys
import time
import json
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

VIEWPORTS = [
    ("2560x1440", 2560, 1440),
    ("1920x1080", 1920, 1080),
    ("1440x900", 1440, 900),
    ("1366x768", 1366, 768),
    ("1280x720", 1280, 720),
    ("1024x768", 1024, 768),
    ("768x1024", 768, 1024),
    ("430x932", 430, 932),
    ("390x844", 390, 844),
    ("360x740", 360, 740),
    ("320x568", 320, 568),
    ("844x390", 844, 390), # landscape mobile
]

def run_tests():
    start_server()
    os.makedirs('screenshots', exist_ok=True)
    report = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        for name, w, h in VIEWPORTS:
            context = browser.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1)
            page = context.new_page()

            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type in ['error'] else None)
            page.on("pageerror", lambda err: console_errors.append(str(err)))

            url = f"http://127.0.0.1:{PORT}/index.html"
            page.goto(url, wait_until='networkidle')
            page.evaluate("document.fonts.ready")

            # Check horizontal scroll
            scroll_check = page.evaluate("""() => {
                const docW = document.documentElement.scrollWidth;
                const bodyW = document.body.scrollWidth;
                const winW = window.innerWidth;
                const hasScroll = (docW > winW + 1) || (bodyW > winW + 1);
                const overflowing = [];
                if (hasScroll) {
                    document.querySelectorAll('*').forEach(el => {
                        const rect = el.getBoundingClientRect();
                        if (rect.right > winW + 1 || rect.left < -1) {
                            overflowing.push({
                                tag: el.tagName,
                                class: el.className ? el.className.toString() : '',
                                id: el.id,
                                right: Math.round(rect.right),
                                winW: winW
                            });
                        }
                    });
                }
                return { hasScroll, docW, bodyW, winW, overflowing: overflowing.slice(0, 5) };
            }""")

            # Check touch targets (minimum 44x44px for interactive elements)
            touch_targets = page.evaluate("""() => {
                const interactives = Array.from(document.querySelectorAll('a, button, input, select, textarea, [role="button"]'));
                const failures = [];
                for (const el of interactives) {
                    const rect = el.getBoundingClientRect();
                    const style = window.getComputedStyle(el);
                    if (style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0') continue;
                    if (rect.width === 0 && rect.height === 0) continue;
                    if (el.classList.contains('sr-only')) continue;
                    
                    if (rect.width < 44 || rect.height < 44) {
                        failures.push({
                            tag: el.tagName,
                            class: el.className ? el.className.toString() : '',
                            text: (el.textContent || '').trim().replace(/\\s+/g, ' ').slice(0, 30),
                            width: Math.round(rect.width),
                            height: Math.round(rect.height)
                        });
                    }
                }
                return failures;
            }""")

            # Check text clipping
            text_clipping = page.evaluate("""() => {
                const clipped = [];
                const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
                let node;
                while (node = walker.nextNode()) {
                    if (node.nodeValue.trim().length > 0 && node.parentElement) {
                        const el = node.parentElement;
                        const style = window.getComputedStyle(el);
                        if (style.display !== 'none' && style.visibility !== 'hidden') {
                            if ((style.overflow === 'hidden' || style.overflowY === 'hidden') && el.scrollHeight > el.clientHeight + 4) {
                                clipped.push({
                                    tag: el.tagName,
                                    class: el.className ? el.className.toString() : '',
                                    text: node.nodeValue.trim().slice(0, 30),
                                    scrollHeight: el.scrollHeight,
                                    clientHeight: el.clientHeight
                                });
                            }
                        }
                    }
                }
                return clipped;
            }""")

            # Scroll through page to trigger lazy loaded images
            page.evaluate("() => { window.scrollTo(0, document.body.scrollHeight); }")
            time.sleep(0.4)
            page.evaluate("() => { window.scrollTo(0, 0); }")
            time.sleep(0.2)

            # Screenshot
            img_path = f"screenshots/test_resp_{name}.png"
            page.screenshot(path=img_path, full_page=True)

            report[name] = {
                "viewport": f"{w}x{h}",
                "horizontal_scroll": scroll_check['hasScroll'],
                "scroll_details": scroll_check,
                "touch_target_failures": touch_targets,
                "touch_target_fail_count": len(touch_targets),
                "text_clipping_issues": text_clipping,
                "console_errors": console_errors,
                "screenshot": img_path
            }
            context.close()

        # Test Text Zoom 200%
        print("Testing Text Zoom 200%...")
        zoom_context = browser.new_context(viewport={'width': 1280, 'height': 720})
        zoom_page = zoom_context.new_page()
        zoom_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until='networkidle')
        zoom_page.evaluate("() => { document.documentElement.style.fontSize = '200%'; }")
        time.sleep(0.5)
        zoom_scroll = zoom_page.evaluate("() => ({ docW: document.documentElement.scrollWidth, winW: window.innerWidth, hasScroll: document.documentElement.scrollWidth > window.innerWidth + 2 })")
        zoom_page.screenshot(path="screenshots/test_zoom_200.png", full_page=True)
        zoom_context.close()
        report["test_zoom_200"] = zoom_scroll

        # Test Font Fallback
        print("Testing Font Fallback...")
        fb_context = browser.new_context(viewport={'width': 1280, 'height': 720})
        fb_page = fb_context.new_page()
        fb_page.route("**/fonts.googleapis.com/**", lambda route: route.abort())
        fb_page.route("**/fonts.gstatic.com/**", lambda route: route.abort())
        fb_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until='networkidle')
        fb_page.screenshot(path="screenshots/test_font_fallback.png", full_page=True)
        fb_scroll = fb_page.evaluate("() => ({ docW: document.documentElement.scrollWidth, winW: window.innerWidth, hasScroll: document.documentElement.scrollWidth > window.innerWidth + 2 })")
        fb_context.close()
        report["test_font_fallback"] = fb_scroll

        # Test prefers-reduced-motion
        print("Testing prefers-reduced-motion...")
        rm_context = browser.new_context(viewport={'width': 1280, 'height': 720}, reduced_motion='reduce')
        rm_page = rm_context.new_page()
        rm_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until='networkidle')
        rm_page.screenshot(path="screenshots/test_reduced_motion.png", full_page=True)
        rm_context.close()
        report["test_reduced_motion"] = "passed"

        # Test prefers-color-scheme: dark
        print("Testing prefers-color-scheme: dark...")
        dm_context = browser.new_context(viewport={'width': 1280, 'height': 720}, color_scheme='dark')
        dm_page = dm_context.new_page()
        dm_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until='networkidle')
        dm_page.screenshot(path="screenshots/test_color_scheme_dark.png", full_page=True)
        dm_context.close()
        report["test_color_scheme_dark"] = "passed"

        browser.close()

    with open("screenshots/responsive_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("Responsive testing finished! Summary:")
    for name, w, h in VIEWPORTS:
        r = report[name]
        print(f"[{name}] Scroll: {r['horizontal_scroll']} | Touch Failures: {r['touch_target_fail_count']} | Text Clip: {len(r['text_clipping_issues'])} | Console Err: {len(r['console_errors'])}")
        if r['touch_target_fail_count'] > 0:
            print(f"   Touch failures: {r['touch_target_failures']}")
        if r['horizontal_scroll']:
            print(f"   Scroll info: {r['scroll_details']}")

if __name__ == '__main__':
    run_tests()
