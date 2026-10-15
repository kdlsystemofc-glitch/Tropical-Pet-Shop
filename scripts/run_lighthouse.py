import os
import sys
import time
import json
import subprocess
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8765

def start_server():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root_dir)
    server = HTTPServer(('127.0.0.1', PORT), SimpleHTTPRequestHandler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    time.sleep(1)

def run():
    start_server()
    os.makedirs('screenshots', exist_ok=True)
    report_path = os.path.abspath('screenshots/lighthouse-report.json')
    
    cmd = [
        'npx.cmd', '--yes', 'lighthouse',
        f'http://127.0.0.1:{PORT}/index.html',
        '--form-factor=mobile',
        '--output=json',
        f'--output-path={report_path}',
        '--chrome-flags=--headless --no-sandbox',
        '--only-categories=performance,accessibility,best-practices,seo'
    ]
    
    print(f"Running Lighthouse CLI: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("STDOUT:", result.stdout[-500:] if result.stdout else "")
    if result.stderr:
        print("STDERR:", result.stderr[-500:])
        
    if not os.path.exists(report_path):
        print("Lighthouse report file not generated!")
        return

    with open(report_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = data.get('categories', {})
    print("\n--- LIGHTHOUSE SCORES (MOBILE) ---")
    for cat_id, cat in categories.items():
        score = int(cat.get('score', 0) * 100) if cat.get('score') is not None else 'N/A'
        print(f"  {cat.get('title', cat_id)}: {score}/100")

    audits = data.get('audits', {})
    opportunities = []
    for audit_id, audit in audits.items():
        details = audit.get('details', {})
        if details.get('type') == 'opportunity':
            overall_savings = details.get('overallSavingsMs', 0)
            overall_bytes = details.get('overallSavingsBytes', 0)
            opportunities.append({
                'id': audit_id,
                'title': audit.get('title'),
                'description': audit.get('description'),
                'score': audit.get('score'),
                'savingsMs': overall_savings,
                'savingsBytes': overall_bytes,
                'displayValue': audit.get('displayValue', '')
            })

    # Sort opportunities by estimated savings ms or score
    opportunities.sort(key=lambda x: (x['savingsMs'], x['savingsBytes']), reverse=True)

    print("\n--- TOP AUDIT OPPORTUNITIES ---")
    for i, opp in enumerate(opportunities[:5], 1):
        disp = opp['displayValue'] if opp['displayValue'] else f"{opp['savingsMs']}ms / {opp['savingsBytes']}B"
        print(f"{i}. {opp['title']} (Savings: {disp})")
        print(f"   Audit ID: {opp['id']}")
        print(f"   Summary: {opp['description'].split('.')[0]}.")

if __name__ == '__main__':
    run()
