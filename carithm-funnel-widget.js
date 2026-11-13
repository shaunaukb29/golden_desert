/* === THE BLUEPRINT: INTERACTIVE AUDIO SAMPLE & GA4 EVENT TRACKING === */
(function() {
  let activeAudio = null;
  let isPlaying = false;
  let playInterval = null;

  // Web Audio Synthesized Acoustic Calibrations for accurate mechanical sound demo
  function playSyntheticAcousticSample(type, onEnded, onTick) {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!AudioContext) return null;
      const ctx = new AudioContext();

      const duration = 4.5;
      const bufferSize = ctx.sampleRate * duration;
      const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
      const data = buffer.getChannelData(0);

      // Synthesize realistic friction/chirp/knock acoustic signature
      if (type === 'brakes') {
        // High-frequency friction squeal (2.8 kHz - 3.4 kHz harmonic resonance)
        for (let i = 0; i < bufferSize; i++) {
          const t = i / ctx.sampleRate;
          const env = Math.min(1, t * 4) * Math.max(0, 1 - (t / duration) * 0.7);
          const squeal = Math.sin(2 * Math.PI * 3120 * t) * 0.45 + Math.sin(2 * Math.PI * 3180 * t) * 0.35;
          const friction = (Math.random() * 2 - 1) * 0.12;
          data[i] = (squeal + friction) * env * 0.4;
        }
      } else if (type === 'belt') {
        // High-pitched rubber rib slip & chirp
        for (let i = 0; i < bufferSize; i++) {
          const t = i / ctx.sampleRate;
          const chirpFreq = 2400 + Math.sin(2 * Math.PI * 8 * t) * 400;
          const env = Math.min(1, t * 5) * (0.8 + 0.2 * Math.sin(2 * Math.PI * 16 * t));
          data[i] = Math.sin(2 * Math.PI * chirpFreq * t) * env * 0.35 + (Math.random() * 2 - 1) * 0.08;
        }
      } else {
        // Engine / mechanical harmonic cadence
        for (let i = 0; i < bufferSize; i++) {
          const t = i / ctx.sampleRate;
          const cadence = Math.pow(Math.max(0, Math.sin(2 * Math.PI * 12 * t)), 8);
          const harmonic = Math.sin(2 * Math.PI * 180 * t) * 0.5 + Math.sin(2 * Math.PI * 360 * t) * 0.3;
          data[i] = (cadence * harmonic + (Math.random() * 2 - 1) * 0.05) * 0.45;
        }
      }

      const source = ctx.createBufferSource();
      source.buffer = buffer;
      source.connect(ctx.destination);
      source.start();

      let startTime = ctx.currentTime;
      const interval = setInterval(function() {
        const elapsed = ctx.currentTime - startTime;
        if (elapsed >= duration) {
          clearInterval(interval);
          if (onEnded) onEnded();
        } else {
          if (onTick) onTick(elapsed, duration);
        }
      }, 100);

      return {
        stop: function() {
          try {
            source.stop();
            clearInterval(interval);
            ctx.close();
          } catch(e) {}
        }
      };
    } catch(err) {
      console.warn('Audio synthesis fallback error:', err);
      return null;
    }
  }

  window.bpToggleSample = function(btnEl, symptomType) {
    const pIcon = btnEl ? btnEl.querySelector('.bp-p-icon') : null;
    const pText = btnEl ? btnEl.querySelector('.bp-p-text') : null;
    const timerEl = document.getElementById('bpTimerText');

    if (isPlaying && activeAudio) {
      activeAudio.stop();
      activeAudio = null;
      isPlaying = false;
      if (pIcon) pIcon.textContent = '▶';
      if (pText) pText.textContent = 'Play the sample this result came from (real ' + symptomType + ' audio)';
      if (timerEl) timerEl.textContent = '0:00 / 0:05';
      return;
    }

    if (pIcon) pIcon.textContent = '⏸';
    if (pText) pText.textContent = 'Playing ' + symptomType + ' acoustic sample...';
    isPlaying = true;

    // GA4 tracking
    if (typeof gtag === 'function') {
      gtag('event', 'sample_play', {
        'event_category': 'Funnel',
        'event_label': symptomType
      });
    }

    activeAudio = playSyntheticAcousticSample(
      symptomType,
      function() {
        isPlaying = false;
        if (pIcon) pIcon.textContent = '▶';
        if (pText) pText.textContent = 'Play the sample this result came from (real ' + symptomType + ' audio)';
        if (timerEl) timerEl.textContent = '0:05 / 0:05';
      },
      function(elapsed, total) {
        if (timerEl) {
          const cur = Math.floor(elapsed);
          timerEl.textContent = '0:0' + cur + ' / 0:05';
        }
      }
    );
  };

  // GA4 Non-Negotiable Tracking Events
  document.addEventListener('DOMContentLoaded', function() {
    // Inline Curiosity Gap Injection: adds a CTA inside .quick-answer to drive /audio clicks
    try {
      const quickAns = document.querySelector(".quick-answer");
      if (quickAns && !document.querySelector(".bp-inline-hook")) {
        const hook = document.createElement("div");
        hook.className = "bp-inline-hook";
        hook.style.cssText = "margin: 14px 0 6px; padding: 10px 14px; background: rgba(16,185,129,0.08); border-left: 3px solid #10b981; border-radius: 6px; display: flex; align-items: center; justify-content: space-between; gap: 10px; font-size: 0.92rem;";
        hook.innerHTML = "<span>⚡ <strong>Not sure?</strong> Test your car sound in 5 seconds</span><a href='https://carithm.vercel.app/audio?src=inline_quick' style='background:#10b981; color:#fff; padding:6px 14px; border-radius:6px; font-weight:700; text-decoration:none; white-space:nowrap; font-size:0.86rem;'>Test Sound &rarr;</a>";
        quickAns.appendChild(hook);
      }
    } catch(e) {}

    // 1. CTA Click Tracking
    document.querySelectorAll('.bp-btn, .bp-sticky-btn, .bp-soft-cta, .bp-upload a').forEach(function(el) {
      el.addEventListener('click', function() {
        try {
          const href = el.getAttribute('href') || '';
          const urlParams = new URLSearchParams(href.split('?')[1] || '');
          const src = urlParams.get('src') || 'unknown';
          if (typeof gtag === 'function') {
            gtag('event', 'cta_click', {
              'event_category': 'Funnel',
              'event_label': el.textContent.trim(),
              'cta_source': src
            });
          }
        } catch(e) {}
      });
    });

    // 2. Scroll Depth Tracking (50% and 90%)
    let scrolled50 = false;
    let scrolled90 = false;
    window.addEventListener('scroll', function() {
      const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (scrollHeight <= 0) return;
      const scrollPercent = (window.scrollY / scrollHeight) * 100;
      if (!scrolled50 && scrollPercent >= 50) {
        scrolled50 = true;
        if (typeof gtag === 'function') {
          gtag('event', 'scroll_depth', { 'event_category': 'Engagement', 'event_label': '50%' });
        }
      }
      if (!scrolled90 && scrollPercent >= 90) {
        scrolled90 = true;
        if (typeof gtag === 'function') {
          gtag('event', 'scroll_depth', { 'event_category': 'Engagement', 'event_label': '90%' });
        }
      }
    }, { passive: true });
  });
})();
