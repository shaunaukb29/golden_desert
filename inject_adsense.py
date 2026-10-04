import os
import re

directory = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"
adsense_script = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5227538935323998" crossorigin="anonymous"></script>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Check if already present
        if "ca-pub-5227538935323998" in content:
            continue
            
        # Insert just before </head>
        content = content.replace('</head>', f'  {adsense_script}\n</head>')
        
        with open(filepath, 'w') as f:
            f.write(content)
        count += 1

print(f"Injected AdSense into {count} files.")
