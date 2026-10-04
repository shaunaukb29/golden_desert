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
desc_1 = "Free engine sound diagnostic AI app. Like Shazam for car noises. Upload your recording for an instant car noise diagnosis from a recording. Diagnose car sounds online."
content_1 = """
<div class="card" style="margin-bottom: 20px;">
    <h2>Like Shazam for Car Noises</h2>
    <p>Wondering what sound your car is making? Our AI acts like Shazam for car sounds. Whether it's a clicking, grinding, or squealing sound, our car noise identifier online tool analyzes the audio and gives you an instant diagnosis.</p>
    
    <h3>Car Noise Diagnosis from a Recording</h3>
    <p>Simply upload an audio or video recording from your phone. Our engine sound diagnostic AI app will process the frequencies to pinpoint exactly what component is failing.</p>
</div>
"""
update_file('/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static/1st.html', desc_1, content_1)

# --- 2nd.html (/) Updates ---
desc_2 = "Carithm AI is a free car sound diagnosis app. Identify engine noise and diagnose car problems instantly. The ultimate AI tool that recognizes car sounds."
content_2 = """
<div class="card" style="margin-bottom: 20px;">
    <h2>Welcome to Carithm AI</h2>
    <p>Carithm is the leading AI-powered free car sound diagnosis app. We help drivers globally identify engine noises and avoid expensive mechanic bills by providing an accurate engine sound check.</p>
    
    <h3>Diagnose Car Problems by Sound</h3>
    <p>Our sophisticated AI engine noise detector listens to your recording and diagnoses car sounds. Discover if your issue is a loose heat shield, a bad wheel bearing, or a failing water pump.</p>
</div>
"""
update_file('/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static/2nd.html', desc_2, content_2)

# --- 3rd.html (/app) Updates ---
desc_3 = "Engine noise analysis app and car sound analysis app. Free engine sound diagnostic AI app with no download required. Run a quick engine sound diagnosis online."
content_3 = """
<div class="card" style="margin-bottom: 20px;">
    <h2>Engine Noise Analysis App</h2>
    <p>Our car sound analysis app uses deep learning to perform an engine sound diagnosis. No download required—just use our web-based engine sound diagnostic AI app directly in your browser.</p>
    
    <h3>Engine Sound Diagnostic AI App</h3>
    <p>Whether you're an auto enthusiast or just a driver trying to fix a problem, our car sound analyzer app gives you dealership-level insights by just listening to your engine.</p>
</div>
"""
update_file('/Users/shaunaukbasu/Desktop/golden_desert/audio/src/cardiag/web/static/3rd.html', desc_3, content_3)

print("Pages updated successfully.")
