import re

def update_file(filename, new_desc, new_content):
    with open(filename, 'r') as f:
        html = f.read()

    # Update meta description
    html = re.sub(r'<meta name="description" content="[^"]+">', f'<meta name="description" content="{new_desc}">', html)

    # Inject new content before the first <div class="card"> or <main> if card not found
    if '<div class="card">' in html:
        html = html.replace('<div class="card">', f'{new_content}\n<div class="card">', 1)
    elif '</main>' in html:
        html = html.replace('</main>', f'{new_content}\n</main>', 1)

    with open(filename, 'w') as f:
        f.write(html)


# --- 1st.html (/audio) Updates ---
# High impressions: engine sound diagnostic ai app (147), car noise diagnosis from recording (101), what is this car sound (62)
# Striking distance: car sound diagnosis (227), car noise detector (144), check engine sound (82)
# Shazam angle: shazam car diagnostic app, shazam for car noises
desc_1 = "Wondering what is this car sound? Free engine sound diagnostic AI app. Upload your recording for an instant car noise diagnosis from a recording. Like Shazam for cars."
content_1 = """
<div class="card" style="margin-bottom: 20px;">
    <h2>What is This Car Sound?</h2>
    <p>Wondering what sound your car is making? Our AI acts like a Shazam car diagnostic app for engine problems. Whether it's a clicking, grinding, or squealing sound, our car noise detector analyzes the audio and gives you an instant check.</p>
    
    <h3>Car Noise Diagnosis from a Recording</h3>
    <p>Simply upload an audio or video recording from your phone. Our engine sound diagnostic AI app will process the frequencies to pinpoint exactly what component is failing, acting as a reliable car sound diagnosis tool.</p>
</div>
"""
update_file('/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static/app.html', desc_1, content_1)

# --- 2nd.html (/) Updates ---
# This page is ranking well for brand (carithm) but has 0-click/low-CTR on:
# engine noise analysis app (36), ai tool that recognizes cars sounds (34), car noise diagnosis (20)
desc_2 = "Carithm AI is the ultimate AI tool that recognizes car sounds. Identify engine noise and get a car noise diagnosis instantly. Free car noise check."
content_2 = """
<div class="card" style="margin-bottom: 20px;">
    <h2>Welcome to Carithm AI</h2>
    <p>Carithm is the leading AI tool that recognizes car sounds. We help drivers globally identify engine noises and avoid expensive mechanic bills by providing an accurate car noise check.</p>
    
    <h3>Diagnose Car Problems by Sound</h3>
    <p>Our sophisticated engine noise analysis app listens to your recording and performs a complete car noise diagnosis. Discover if your issue is a loose heat shield, a bad wheel bearing, or a failing water pump.</p>
</div>
"""
update_file('/Users/shaunaukbasu/Desktop/golden_desert/index.html', desc_2, content_2)

# --- 3rd.html (/app) Updates ---
# Impressions: engine sound diagnostic ai app (86), engine noise analysis app (17), car noise identifier online free (13)
desc_3 = "Engine noise analysis app. A free engine sound diagnostic AI app with no download required. Run a quick car noise identifier online free check."
content_3 = """
<div class="card" style="margin-bottom: 20px;">
    <h2>Engine Noise Analysis App</h2>
    <p>Our car sound analysis app uses deep learning to perform an engine sound diagnosis. No download required—just use our web-based engine sound diagnostic AI app directly in your browser.</p>
    
    <h3>Car Noise Identifier Online Free</h3>
    <p>Whether you're an auto enthusiast or just a driver trying to fix a problem, our car sound analyzer app gives you dealership-level insights by just listening to your engine. It's completely free to use online.</p>
</div>
"""
update_file('/Users/shaunaukbasu/Desktop/golden_desert/app/index.html', desc_3, content_3)

print("Pages updated successfully.")
