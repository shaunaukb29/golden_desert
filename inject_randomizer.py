import os
import re

directory = "/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static"
script_to_inject = """
<script>
  (function() {
    var links = [
      "https://hadi10973-nmanvbz9onaxzbwzdmnjku.streamlit.app/?embed=true",
      "https://heidi23982-5vovybvpxghzdhuduaairo.streamlit.app/?embed=true",
      "https://heimi34505-3aue9zwjqykkgwxjwnemcy.streamlit.app/?embed=true"
    ];
    var iframe = document.getElementById("streamlitFrame") || document.querySelector("iframe.streamlit-embed");
    if (iframe) {
      iframe.src = links[Math.floor(Math.random() * links.length)];
    }
  })();
</script>"""

count = 0

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Check if already injected
        if "hadi10973-nmanvbz9onaxzbwzdmnjku" in content:
            continue
            
        # Replace the src in iframe
        content = re.sub(r'src="https://[^"]+\.streamlit\.app/[^"]*"', 'src="about:blank"', content)
        
        # Inject script after </iframe>
        content = re.sub(r'(</iframe>)', r'\1' + script_to_inject, content)
        
        with open(filepath, 'w') as f:
            f.write(content)
        count += 1

print(f"Injected randomizer script into {count} files.")
