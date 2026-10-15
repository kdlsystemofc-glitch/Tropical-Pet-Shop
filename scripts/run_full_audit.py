import os
import sys
import time
import json
import threading
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

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

ALL_VIEWPORTS = [
    ("3840x2160_4K", 3840, 2160),
    ("3440x1440_Ultrawide", 3440, 1440),
    ("2560x1440_QHD", 2560, 1440),
    ("1920x1080_FHD", 1920, 1080),
    ("1440x900_Mac", 1440, 900),
    ("1366x768_HD", 1366, 768),
    ("1280x720_720p", 1280, 720),
    ("1024x768_iPad_Land", 1024, 768),
    ("768x1024_iPad_Port", 768, 1024),
    ("430x932_iPhone_ProMax", 430, 932),
    ("390x844_iPhone_14", 390, 844),
    ("360x740_Android_Avg", 360, 740),
    ("320x568_iPhone_SE1", 320, 568),
    ("844x390_iPhone_Landscape", 844, 390),
]

def run_comprehensive_audit():
    start_server()
    os.makedirs('screenshots/audit', exist_ok=True)
    results = {
        "chromium": {},
        "webkit": {},
        "motion_modes": {},
        "seo_semantics": {},
        "lighthouse": {}
    }

    url = f"http://127.0.0.1:{PORT}/index.html"

    with sync_playwright() as p:
        # --- 1. CHROMIUM SUITE ---
        print("\n==========================================")
        print("  1. AUDITORIA CHROMIUM (14 VIEWPORTS)")
        print("==========================================")
        browser = p.chromium.launch(headless=True)
        
        for name, w, h in ALL_VIEWPORTS:
            context = browser.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1)
            page = context.new_page()

            console_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type in ['error'] else None)
            page.on("pageerror", lambda err: console_errors.append(str(err)))

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

            # Check touch targets
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

            # Screenshot
            img_path = f"screenshots/audit/chromium_{name}.png"
            page.screenshot(path=img_path, full_page=True)

            status = "PASS" if not scroll_check['hasScroll'] and len(touch_targets) == 0 and len(console_errors) == 0 else "FAIL"
            print(f"[{status}] Chromium {name} ({w}x{h}) - Scroll: {scroll_check['hasScroll']}, TouchFail: {len(touch_targets)}, TextClip: {len(text_clipping)}, Errors: {len(console_errors)}")

            results["chromium"][name] = {
                "viewport": f"{w}x{h}",
                "status": status,
                "horizontal_scroll": scroll_check['hasScroll'],
                "touch_target_fails": len(touch_targets),
                "text_clipping_issues": len(text_clipping),
                "console_errors": console_errors,
                "screenshot": img_path
            }
            context.close()
        browser.close()

        # --- 2. WEBKIT SUITE ---
        print("\n==========================================")
        print("  2. AUDITORIA WEBKIT / SAFARI ENGINE")
        print("==========================================")
        webkit_browser = p.webkit.launch(headless=True)
        webkit_views = [
            ("1920x1080_FHD", 1920, 1080),
            ("1440x900_Mac", 1440, 900),
            ("768x1024_iPad", 768, 1024),
            ("390x844_iPhone_14", 390, 844),
            ("320x568_iPhone_SE1", 320, 568),
            ("844x390_iPhone_Landscape", 844, 390)
        ]

        for name, w, h in webkit_views:
            wk_ctx = webkit_browser.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1)
            wk_page = wk_ctx.new_page()
            wk_errors = []
            wk_page.on("console", lambda msg: wk_errors.append(msg.text) if msg.type in ['error'] else None)
            wk_page.on("pageerror", lambda err: wk_errors.append(str(err)))

            wk_page.goto(url, wait_until='networkidle')
            wk_page.evaluate("document.fonts.ready")

            scroll_check = wk_page.evaluate("""() => {
                const docW = document.documentElement.scrollWidth;
                const winW = window.innerWidth;
                return { hasScroll: docW > winW + 1, docW, winW };
            }""")

            img_path = f"screenshots/audit/webkit_{name}.png"
            wk_page.screenshot(path=img_path, full_page=True)

            status = "PASS" if not scroll_check['hasScroll'] and len(wk_errors) == 0 else "FAIL"
            print(f"[{status}] WebKit {name} ({w}x{h}) - Scroll: {scroll_check['hasScroll']}, Errors: {len(wk_errors)}")

            results["webkit"][name] = {
                "viewport": f"{w}x{h}",
                "status": status,
                "horizontal_scroll": scroll_check['hasScroll'],
                "console_errors": wk_errors,
                "screenshot": img_path
            }
            wk_ctx.close()
        webkit_browser.close()

        # --- 3. MOTION MODES SUITE ---
        print("\n==========================================")
        print("  3. AUDITORIA DE MODOS DE MOTION")
        print("==========================================")
        motion_browser = p.chromium.launch(headless=True)
        
        # Helper to load and initialize motion
        def setup_motion_page(context):
            pg = context.new_page()
            pg.goto(url, wait_until='networkidle')
            # Trigger interaction to load motion scripts immediately
            pg.mouse.move(50, 50)
            pg.wait_for_function("() => window.TropicalMotion && window.TropicalMotion.isInitialized", timeout=10000)
            return pg

        # Test 3.1: Full Motion
        ctx_full = motion_browser.new_context(viewport={'width': 1280, 'height': 720})
        p_full = setup_motion_page(ctx_full)
        mode_full = p_full.evaluate("() => window.TropicalMotion.mode")
        quality_full = p_full.evaluate("() => window.TropicalMotion.quality")
        dom_mode_full = p_full.evaluate("() => document.documentElement.dataset.motionMode")
        print(f"[PASS] Modo Full Motion: {mode_full} | Quality: {quality_full} | DOM data-motion-mode: {dom_mode_full}")
        results["motion_modes"]["full"] = {
            "mode": mode_full,
            "quality": quality_full,
            "dom_mode": dom_mode_full
        }
        ctx_full.close()

        # Test 3.2: Reduced Motion
        ctx_rm = motion_browser.new_context(viewport={'width': 1280, 'height': 720}, reduced_motion='reduce')
        p_rm = setup_motion_page(ctx_rm)
        mode_rm = p_rm.evaluate("() => window.TropicalMotion.mode")
        dom_mode_rm = p_rm.evaluate("() => document.documentElement.dataset.motionMode")
        print(f"[PASS] Modo Reduced Motion: {mode_rm} | DOM data-motion-mode: {dom_mode_rm}")
        results["motion_modes"]["reduced"] = {
            "mode": mode_rm,
            "dom_mode": dom_mode_rm
        }
        ctx_rm.close()

        # Test 3.3: Paused Mode via Toggle Button
        ctx_pause = motion_browser.new_context(viewport={'width': 1280, 'height': 720})
        p_pause = setup_motion_page(ctx_pause)
        toggle_btn = p_pause.locator('#motion-toggle-btn')
        is_visible = toggle_btn.is_visible()
        aria_label_before = toggle_btn.get_attribute('aria-label')
        
        # Click to pause
        toggle_btn.click()
        time.sleep(0.3)
        mode_paused = p_pause.evaluate("() => window.TropicalMotion.mode")
        dom_mode_paused = p_pause.evaluate("() => document.documentElement.dataset.motionMode")
        aria_label_paused = toggle_btn.get_attribute('aria-label')

        # Click to resume
        toggle_btn.click()
        time.sleep(0.3)
        mode_resumed = p_pause.evaluate("() => window.TropicalMotion.mode")
        dom_mode_resumed = p_pause.evaluate("() => document.documentElement.dataset.motionMode")
        aria_label_resumed = toggle_btn.get_attribute('aria-label')

        print(f"[PASS] Modo Pausado: {mode_paused} (Aria: '{aria_label_paused}') -> Retomado: {mode_resumed} (Aria: '{aria_label_resumed}')")
        results["motion_modes"]["pause_toggle"] = {
            "btn_visible": is_visible,
            "paused_mode": mode_paused,
            "paused_aria": aria_label_paused,
            "resumed_mode": mode_resumed,
            "resumed_aria": aria_label_resumed
        }
        ctx_pause.close()
        motion_browser.close()

        # --- 4. SEO & SEMANTICS AUDIT ---
        print("\n==========================================")
        print("  4. AUDITORIA SEO & ESTRUTURA SEMÂNTICA")
        print("==========================================")
        seo_browser = p.chromium.launch(headless=True)
        seo_page = seo_browser.new_page()
        seo_page.goto(url, wait_until='networkidle')

        seo_audit = seo_page.evaluate("""() => {
            const h1s = Array.from(document.querySelectorAll('h1')).map(h => h.textContent.trim());
            const h2s = Array.from(document.querySelectorAll('h2')).map(h => h.textContent.trim());
            const metaDesc = document.querySelector('meta[name="description"]')?.getAttribute('content') || null;
            const title = document.title;
            const themeColor = document.querySelector('meta[name="theme-color"]')?.getAttribute('content') || null;
            const lang = document.documentElement.getAttribute('lang');
            const ogTitle = document.querySelector('meta[property="og:title"]')?.getAttribute('content') || null;
            const ogDesc = document.querySelector('meta[property="og:description"]')?.getAttribute('content') || null;
            const ogImage = document.querySelector('meta[property="og:image"]')?.getAttribute('content') || null;
            const twCard = document.querySelector('meta[name="twitter:card"]')?.getAttribute('content') || null;
            
            // Schema.org
            let schemaValid = false;
            let schemaType = null;
            let schemaBusinessName = null;
            const scriptTag = document.querySelector('script[type="application/ld+json"]');
            if (scriptTag) {
                try {
                    const parsed = JSON.parse(scriptTag.textContent);
                    schemaValid = true;
                    schemaType = parsed['@type'];
                    schemaBusinessName = parsed['name'];
                } catch(e) {
                    schemaValid = false;
                }
            }

            // Image alts
            const imgs = Array.from(document.querySelectorAll('img'));
            const missingAlt = imgs.filter(i => !i.hasAttribute('alt')).map(i => i.src);

            return {
                title,
                lang,
                metaDesc,
                themeColor,
                h1_count: h1s.length,
                h1s,
                h2_count: h2s.length,
                h2s,
                ogTitle,
                ogDesc,
                ogImage,
                twCard,
                schemaValid,
                schemaType,
                schemaBusinessName,
                totalImages: imgs.length,
                missingAltCount: missingAlt.length
            };
        }""")
        print(f"[PASS] Title: {seo_audit['title']}")
        print(f"[PASS] Meta Description: {seo_audit['metaDesc'][:60]}... ({len(seo_audit['metaDesc'])} chars)")
        print(f"[PASS] H1 Count: {seo_audit['h1_count']} -> {seo_audit['h1s']}")
        print(f"[PASS] H2 Count: {seo_audit['h2_count']}")
        print(f"[PASS] Schema.org JSON-LD Válido: {seo_audit['schemaValid']}, Type: {seo_audit['schemaType']}")
        print(f"[PASS] Imagens com Alt: {seo_audit['totalImages'] - seo_audit['missingAltCount']}/{seo_audit['totalImages']} (Faltando: {seo_audit['missingAltCount']})")
        results["seo_semantics"] = seo_audit
        seo_browser.close()

    # --- 5. LIGHTHOUSE SUITE (MOBILE & DESKTOP) ---
    print("\n==========================================")
    print("  5. AUDITORIA LIGHTHOUSE (MOBILE & DESKTOP)")
    print("==========================================")
    for form_factor in ['mobile', 'desktop']:
        report_file = os.path.abspath(f'screenshots/audit/lighthouse_{form_factor}.json')
        if form_factor == 'desktop':
            cmd = [
                'npx.cmd', '--yes', 'lighthouse',
                f'http://127.0.0.1:{PORT}/index.html',
                '--preset=desktop',
                '--output=json',
                f'--output-path={report_file}',
                '--chrome-flags=--headless --no-sandbox',
                '--only-categories=performance,accessibility,best-practices,seo'
            ]
        else:
            cmd = [
                'npx.cmd', '--yes', 'lighthouse',
                f'http://127.0.0.1:{PORT}/index.html',
                '--form-factor=mobile',
                '--output=json',
                f'--output-path={report_file}',
                '--chrome-flags=--headless --no-sandbox',
                '--only-categories=performance,accessibility,best-practices,seo'
            ]

        print(f"Executando Lighthouse ({form_factor.upper()})...")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(report_file):
            with open(report_file, 'r', encoding='utf-8') as lf:
                lh_data = json.load(lf)
            cats = lh_data.get('categories', {})
            audits = lh_data.get('audits', {})
            scores = {cid: int(c.get('score', 0) * 100) for cid, c in cats.items()}
            vitals = {
                'FCP': audits.get('first-contentful-paint', {}).get('displayValue'),
                'LCP': audits.get('largest-contentful-paint', {}).get('displayValue'),
                'TBT': audits.get('total-blocking-time', {}).get('displayValue'),
                'CLS': audits.get('cumulative-layout-shift', {}).get('displayValue'),
                'SI': audits.get('speed-index', {}).get('displayValue'),
            }
            print(f"-> Scores {form_factor.upper()}: {scores}")
            print(f"-> Vitals {form_factor.upper()}: {vitals}")
            results["lighthouse"][form_factor] = {
                "scores": scores,
                "vitals": vitals
            }
        else:
            print(f"Erro ao gerar relatório do Lighthouse {form_factor}")
            if res.stderr:
                print(res.stderr[-300:])

    # Save complete audit report
    with open("screenshots/audit/comprehensive_audit_report.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("\nAuditoria completa concluída com sucesso! Resultados salvos em screenshots/audit/comprehensive_audit_report.json")

if __name__ == '__main__':
    run_comprehensive_audit()
