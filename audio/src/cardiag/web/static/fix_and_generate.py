import os
import glob
import re

ad_script = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5227538935323998" crossorigin="anonymous"></script>'
gtag_script = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-TCCEJ6DCM1"></script>'

files = glob.glob('*.html')
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    if 'adsbygoogle.js' not in content and gtag_script in content:
        content = content.replace(gtag_script, f"{gtag_script}\n{ad_script}")
        with open(file, 'w') as f:
            f.write(content)

print(f"Fixed AdSense in {len(files)} files.")
