import sys
import time
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
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

def test_section(section_id):
    start_server()
    os.makedirs('screenshots/motion', exist_ok=True)
    report = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
        page.on("pageerror", lambda err: console_errors.append(str(err)))

        url = f"http://127.0.0.1:{PORT}/index.html"
        page.goto(url, wait_until='networkidle')
        page.evaluate("document.fonts.ready")

        # 1. Capture settled state of target section
        sec_el = page.locator(f"#{section_id}")
        if sec_el.count() == 0:
            print(f"Error: Section #{section_id} not found!")
            return False

        sec_el.scroll_into_view_if_needed()
        time.sleep(1.2) # wait for entrance animation to settle

        settled_shot = f"screenshots/motion/{section_id}-settled.png"
        sec_el.screenshot(path=settled_shot)
        print(f"Captured settled screenshot: {settled_shot}")

        # 2. Fast scroll stress test (nothing stuck or hidden)
        print("Running fast scroll stress test...")
        page.evaluate("""() => {
            window.scrollTo(0, document.body.scrollHeight);
        }""")
        time.sleep(0.3)
        page.evaluate("""() => {
            window.scrollTo(0, 0);
        }""")
        time.sleep(0.3)
        sec_el.scroll_into_view_if_needed()
        time.sleep(0.8)

        # Check visibility of all children inside section
        hidden_elements = page.evaluate(f"""() => {{
            const sec = document.getElementById('{section_id}');
            if (!sec) return [];
            const issues = [];
            const elements = sec.querySelectorAll('h1, h2, h3, h4, p, a, button, img');
            elements.forEach(el => {{
                const style = window.getComputedStyle(el);
                const rect = el.getBoundingClientRect();
                const opacity = parseFloat(style.opacity);
                const visibility = style.visibility;
                if (opacity < 0.95 || visibility === 'hidden') {{
                    issues.push({{
                        tag: el.tagName,
                        class: el.className,
                        opacity: opacity,
                        visibility: visibility,
                        text: (el.textContent || '').trim().slice(0, 25)
                    }});
                }}
            }});
            return issues;
        }}""")

        # 3. Check Stacking Context Integrity (Blobs cannot have transform/filter ancestors)
        stacking_issues = page.evaluate("""() => {
            const blobs = document.querySelectorAll('.hero-blob-wrapper, .services-blob-wrapper, .products-blob-wrapper, .reviews-blob-wrapper');
            const issues = [];
            blobs.forEach(b => {
                let parent = b.parentElement;
                while (parent && parent !== document.body) {
                    const style = window.getComputedStyle(parent);
                    if (style.transform !== 'none' || style.filter !== 'none' || parseFloat(style.opacity) < 1) {
                        issues.push({
                            blob: b.className,
                            parent: parent.tagName + '.' + parent.className,
                            transform: style.transform,
                            filter: style.filter,
                            opacity: style.opacity
                        });
                    }
                    parent = parent.parentElement;
                }
            });
            return issues;
        }""")

        report = {
            "section": section_id,
            "settled_screenshot": settled_shot,
            "hidden_elements_count": len(hidden_elements),
            "hidden_elements": hidden_elements,
            "stacking_issues_count": len(stacking_issues),
            "stacking_issues": stacking_issues,
            "console_errors": console_errors
        }

        print(f"[{section_id}] Fast scroll hidden issues: {len(hidden_elements)} | Stacking issues: {len(stacking_issues)} | Console errors: {len(console_errors)}")
        if hidden_elements:
            print("  Hidden items:", hidden_elements)
        if stacking_issues:
            print("  Stacking issues:", stacking_issues)

        browser.close()

    return len(hidden_elements) == 0 and len(stacking_issues) == 0 and len(console_errors) == 0

if __name__ == '__main__':
    sec = sys.argv[1] if len(sys.argv) > 1 else 'hero'
    ok = test_section(sec)
    sys.exit(0 if ok else 1)
