import os
import subprocess

scripts = ['site/js/motion-core.js', 'site/js/motion-sections.js']

print("=== JAVASCRIPT WEIGHT REPORT ===")
for s in scripts:
    min_path = s.replace('.js', '.min.js')
    cmd = f"npx terser \"{s}\" -o \"{min_path}\" --compress --mangle"
    subprocess.run(cmd, shell=True, check=True)
    
    orig_kb = os.path.getsize(s) / 1024
    min_kb = os.path.getsize(min_path) / 1024
    print(f"  {s}: {orig_kb:.1f} KiB -> {min_path}: {min_kb:.1f} KiB ({(1 - min_kb/orig_kb)*100:.1f}% reduction)")

for v in ['site/js/vendor/gsap.min.js', 'site/js/vendor/ScrollTrigger.min.js', 'site/js/vendor/lenis.min.js']:
    if os.path.exists(v):
        size_kb = os.path.getsize(v) / 1024
        print(f"  [Vendor] {v}: {size_kb:.1f} KiB")
