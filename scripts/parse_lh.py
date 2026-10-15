import json

with open('screenshots/lighthouse-report.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

audits = d.get('audits', {})

print("=== CORE WEB VITALS (MOBILE) ===")
for k in ['first-contentful-paint', 'largest-contentful-paint', 'total-blocking-time', 'cumulative-layout-shift', 'speed-index']:
    if k in audits:
        print(f"  {k}: {audits[k].get('displayValue', '')} (score: {audits[k].get('score')})")

print("\n=== LOW SCORE AUDITS (< 0.9) ===")
low_audits = []
for k, v in audits.items():
    score = v.get('score')
    if score is not None and score < 0.9:
        low_audits.append((k, score, v.get('title', ''), v.get('displayValue', '')))

low_audits.sort(key=lambda x: (x[1] if x[1] is not None else 1))
for k, score, title, disp in low_audits:
    print(f"  [{k}] (score: {score}) {title} -> {disp}")
