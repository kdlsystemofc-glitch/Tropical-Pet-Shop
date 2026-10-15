import re

css = open('site/css/critical.min.css', 'r', encoding='utf-8').read()
html = open('index.html', 'r', encoding='utf-8').read()

html = re.sub(r'<style id="critical-css">[\s\S]*?</style>', f'<style id="critical-css">{css}</style>', html)
open('index.html', 'w', encoding='utf-8').write(html)
print("Updated index.html critical CSS!")
