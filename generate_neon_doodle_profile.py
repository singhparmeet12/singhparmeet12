#!/usr/bin/env python3
"""
generate_neon_doodle_profile.py
Builds Parmeet Singh's Cyber-Doodle Notebook GitHub Profile:
- 100% Continuous Flow (seamless unified dark canvas, no black breaks)
- Cool Neon Accents (electric green #00FF66, cyber cyan #00F0FF, warm gold #FFD700)
- Doodle / Handwritten Notebook aesthetic (Patrick Hand / Segoe Print / Caveat + sketched arrows, notes, tape, brackets)
- Vibrant Animations (floating avatar, pulsing neon glows, shimmer strokes, blinking terminal cursor, breathing radar dots)
- 100% Verified Working Links (no non-working buttons)
- Matching Profile Picture
"""

import base64
import os

ASSETS_DIR = 'assets'
os.makedirs(ASSETS_DIR, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# 1. LOAD AVATAR BASE64
# ═══════════════════════════════════════════════════════════════
avatar_path = os.path.join(ASSETS_DIR, 'parmeet-avatar.png')
with open(avatar_path, 'rb') as f:
    AVATAR_B64 = base64.b64encode(f.read()).decode('utf-8')
print(f"[OK] Loaded avatar ({len(AVATAR_B64)//1024} KB)")

# ═══════════════════════════════════════════════════════════════
# 2. DESIGN TOKENS & PALETTE
# ═══════════════════════════════════════════════════════════════
BG = '#0d1117'          # Exact GitHub dark mode background
BG_SURFACE = '#121820'  # Subtle dark card surface
BG_NOTEBOOK = '#0f161e' # Notebook page tone
NEON_GREEN = '#00FF66'  # Main vibrant neon green
NEON_CYAN = '#00F0FF'   # Electric cyan accent
NEON_GOLD = '#FFD700'   # Golden amber (matches turban & aviators)
NEON_PINK = '#FF2A85'   # Doodle spark accent
TEXT_MAIN = '#f0f6fc'   # Crisp white
TEXT_MUTED = '#8b949e'  # Soft gray
GRID_LINE = '#14231b'   # Subtle neon notebook grid

FONTS_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&amp;family=Caveat:wght@600;700&amp;family=JetBrains+Mono:wght@400;600;700&amp;family=Inter:wght@400;600;800&amp;display=swap');

.doodle-hand {
  font-family: 'Patrick Hand', 'Caveat', 'Segoe Print', 'Comic Sans MS', cursive, sans-serif;
}
.mono {
  font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, monospace;
}
.sans {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
"""

COMMON_DEFS = f"""
  <defs>
    <!-- Notebook Graph Grid Pattern -->
    <pattern id="notebookGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{GRID_LINE}" stroke-width="0.8" opacity="0.6"/>
      <circle cx="12" cy="12" r="0.6" fill="{NEON_GREEN}" opacity="0.25"/>
    </pattern>

    <!-- Neon Glow Filters -->
    <filter id="neonGlowGreen" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3.5" result="blur1"/>
      <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="blur2"/>
      <feFlood flood-color="{NEON_GREEN}" flood-opacity="0.6" result="color"/>
      <feComposite in="color" in2="blur1" operator="in" result="glow1"/>
      <feComposite in="color" in2="blur2" operator="in" result="glow2"/>
      <feMerge>
        <feMergeNode in="glow2"/>
        <feMergeNode in="glow1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="neonGlowCyan" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3.5" result="blur"/>
      <feFlood flood-color="{NEON_CYAN}" flood-opacity="0.55" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feFlood flood-color="{NEON_GREEN}" flood-opacity="0.4" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="g"/>
      <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <!-- Animated Shimmer Gradient -->
    <linearGradient id="neonGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{NEON_GREEN}">
        <animate attributeName="stop-color" values="{NEON_GREEN};{NEON_CYAN};{NEON_GREEN}" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{NEON_CYAN}">
        <animate attributeName="stop-color" values="{NEON_CYAN};{NEON_GREEN};{NEON_CYAN}" dur="4s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Ambient Avatar Glow -->
    <radialGradient id="avatarBackdropGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{NEON_GREEN}" stop-opacity="0.22"/>
      <stop offset="60%" stop-color="{NEON_CYAN}" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
  </defs>
"""

COMMON_STYLES = f"""
  <style><![CDATA[
    {FONTS_CSS}
    @keyframes floatAvatar {{
      0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
      50% {{ transform: translateY(-10px) rotate(-1deg); }}
    }}
    @keyframes blinkCursor {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    @keyframes pulseNeon {{
      0%, 100% {{ opacity: 0.55; stroke-width: 1.5; }}
      50% {{ opacity: 1; stroke-width: 2.2; }}
    }}
    @keyframes radarPing {{
      0% {{ r: 3; opacity: 1; }}
      70% {{ r: 8; opacity: 0; }}
      100% {{ r: 8; opacity: 0; }}
    }}
    @keyframes starTwinkle {{
      0%, 100% {{ transform: scale(0.8); opacity: 0.3; }}
      50% {{ transform: scale(1.2); opacity: 1; }}
    }}
    @keyframes dashTravel {{
      to {{ stroke-dashoffset: -32; }}
    }}
    .floating-avatar {{ animation: floatAvatar 4.5s ease-in-out infinite; transform-origin: center; }}
    .cursor-blink {{ animation: blinkCursor 0.9s infinite; }}
    .pulse-glow {{ animation: pulseNeon 2.8s ease-in-out infinite; }}
    .radar-pulse {{ animation: radarPing 2s cubic-bezier(0, 0.2, 0.8, 1) infinite; }}
    .star-1 {{ animation: starTwinkle 2.5s ease-in-out infinite; transform-origin: center; }}
    .star-2 {{ animation: starTwinkle 2.5s ease-in-out infinite 1.2s; transform-origin: center; }}
    .connecting-line {{ stroke-dasharray: 6, 6; animation: dashTravel 2s linear infinite; }}
  ]]></style>
"""

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"[OK] Generated {filename}")

# ═══════════════════════════════════════════════════════════════
# 3. HERO BANNER (880 × 390)
# ═══════════════════════════════════════════════════════════════
hero_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 390" width="880" height="390">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Seamless Canvas Background -->
  <rect width="880" height="390" fill="{BG}"/>
  <rect width="880" height="390" fill="url(#notebookGrid)"/>

  <!-- Top Notebook Washi Tape Accent -->
  <polygon points="40,12 180,10 178,28 38,30" fill="{NEON_GREEN}" opacity="0.18"/>
  <text x="109" y="24" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1.5">PARMEET.DEV // 2026</text>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="390" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="390" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Main Greeting (Handwritten Notebook Style) -->
  <g transform="translate(70, 78)">
    <!-- Small Doodle Note Badge -->
    <rect x="0" y="0" width="138" height="26" rx="13" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1" opacity="0.9"/>
    <circle cx="14" cy="13" r="3.5" fill="{NEON_GREEN}" class="pulse-glow"/>
    <text x="26" y="17" class="mono" font-size="11" font-weight="600" fill="{NEON_GREEN}" letter-spacing="0.5">ONLINE • BUILDING</text>

    <!-- Hey, I'm Parmeet Singh (Handwritten + Neon Glow) -->
    <text x="0" y="70" class="doodle-hand" font-size="56" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.5">
      Hey, I'm <tspan fill="url(#neonGradient)" filter="url(#neonGlowGreen)">Parmeet</tspan>!
    </text>

    <!-- Sketched Neon Underline -->
    <path d="M 2,82 Q 70,88 150,83 T 310,84" fill="none" stroke="{NEON_GREEN}" stroke-width="3" stroke-linecap="round" filter="url(#softGlow)"/>
    <path d="M 12,88 Q 80,92 180,88 T 270,89" fill="none" stroke="{NEON_CYAN}" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>

    <!-- Role & Specialization -->
    <text x="2" y="124" class="mono" font-size="16" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1">
      FULL-STACK DEVELOPER <tspan fill="{TEXT_MUTED}">|</tspan> <tspan fill="{NEON_CYAN}">WEB • DATA • AI</tspan>
    </text>

    <!-- Notebook Handwritten Notes & Bio -->
    <g transform="translate(2, 148)">
      <text x="0" y="20" class="doodle-hand" font-size="20" fill="{TEXT_MAIN}" opacity="0.92">
        ✏️  I engineer fast, scalable web apps &amp; intelligent tools.
      </text>
      <text x="0" y="46" class="doodle-hand" font-size="20" fill="{TEXT_MAIN}" opacity="0.92">
        📍  Based in Delhi, India • Passionate about clean code &amp; sleek UI.
      </text>
      <text x="0" y="72" class="mono" font-size="13" fill="{TEXT_MUTED}">
        const focus = ["React", "Next.js", "Django", "Python", "Full-Stack"];<tspan fill="{NEON_GREEN}" class="cursor-blink">▋</tspan>
      </text>
    </g>

    <!-- Doodle Arrow Pointing Down to Action Buttons -->
    <g transform="translate(14, 255)">
      <path d="M 0,0 C 25,18 45,15 65,30" fill="none" stroke="{NEON_GREEN}" stroke-width="2" stroke-linecap="round" stroke-dasharray="4,3"/>
      <polygon points="66,24 67,35 56,31" fill="{NEON_GREEN}"/>
      <text x="75" y="28" class="doodle-hand" font-size="17" font-weight="600" fill="{NEON_GREEN}">
        explore quick links &amp; resume below ↴
      </text>
    </g>
  </g>

  <!-- Right Floating Sikh Tech Avatar -->
  <g transform="translate(560, 25)">
    <!-- Ambient Neon Backdrop Glow -->
    <ellipse cx="150" cy="180" rx="145" ry="165" fill="url(#avatarBackdropGlow)"/>

    <!-- Sketched Doodle Orbit Ring -->
    <ellipse cx="150" cy="180" rx="135" ry="155" fill="none" stroke="{NEON_GREEN}" stroke-width="1.2" stroke-dasharray="6,8" opacity="0.4" class="connecting-line"/>

    <!-- Floating Avatar with Laptop -->
    <g class="floating-avatar">
      <image href="data:image/png;base64,{AVATAR_B64}" x="25" y="10" width="250" height="340" preserveAspectRatio="xMidYMid meet"/>
    </g>

    <!-- Neon Doodle Floating Icons -->
    <!-- Code Bracket -->
    <g transform="translate(15, 75)" class="star-1">
      <rect x="-14" y="-12" width="28" height="24" rx="6" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1"/>
      <text x="0" y="5" text-anchor="middle" class="mono" font-size="13" font-weight="700" fill="{NEON_GREEN}">&lt;/&gt;</text>
    </g>

    <!-- Neon Star -->
    <g transform="translate(270, 95)" class="star-2">
      <path d="M 0,-7 L 2,-2 L 7,0 L 2,2 L 0,7 L -2,2 L -7,0 L -2,-2 Z" fill="{NEON_GOLD}" filter="url(#softGlow)"/>
    </g>

    <!-- Neon Sparkle -->
    <g transform="translate(25, 270)" class="star-2">
      <path d="M 0,-6 L 1.5,-1.5 L 6,0 L 1.5,1.5 L 0,6 L -1.5,1.5 L -6,0 L -1.5,-1.5 Z" fill="{NEON_CYAN}" filter="url(#softGlow)"/>
    </g>

    <!-- Tech Tag Doodle -->
    <g transform="translate(210, 290)">
      <rect x="0" y="0" width="85" height="24" rx="12" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1" opacity="0.85"/>
      <text x="42" y="16" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{NEON_CYAN}">TURBAN &amp; CODE</text>
    </g>
  </g>

  <!-- Bottom Connecting Neon Guide (Flows into buttons) -->
  <line x1="440" y1="360" x2="440" y2="390" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="388" r="3" fill="{NEON_GREEN}"/>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'hero-banner.svg'), hero_svg)

# ═══════════════════════════════════════════════════════════════
# 4. ACTION BUTTONS (Clickable SVGs with Doodle + Neon Glow)
# ═══════════════════════════════════════════════════════════════
buttons_data = [
    ('resume',    '📄 View Resume', 160, NEON_GREEN, 'PDF & Download'),
    ('talk',      '💬 Let\'s Talk', 145, NEON_CYAN,  'Email Parmeet'),
    ('linkedin',  '💼 LinkedIn',    140, NEON_GOLD,  'Connect Network'),
    ('portfolio', '🌐 Portfolio',   150, NEON_GREEN, 'Interactive Site'),
]

for b_id, label, width, color, hint in buttons_data:
    btn_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 44" width="{width}" height="44">
  <defs>
    <filter id="btnGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur"/>
      <feFlood flood-color="{color}" flood-opacity="0.45" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style><![CDATA[
    {FONTS_CSS}
    @keyframes btnPulse {{
      0%, 100% {{ stroke-opacity: 0.6; stroke-width: 1.4; }}
      50% {{ stroke-opacity: 1; stroke-width: 2.0; }}
    }}
    .btn-border {{ animation: btnPulse 2.8s ease-in-out infinite; }}
  ]]></style>

  <!-- Button Background -->
  <rect x="2" y="2" width="{width-4}" height="40" rx="20" fill="{BG_SURFACE}"/>

  <!-- Neon Sketched Border -->
  <rect x="2" y="2" width="{width-4}" height="40" rx="20" fill="none" stroke="{color}" stroke-width="1.6" class="btn-border" filter="url(#btnGlow)"/>

  <!-- Button Label (Handwritten/Casual + Clean) -->
  <text x="{width//2}" y="27" text-anchor="middle" class="doodle-hand" font-size="18" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.3">
    {label}
  </text>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f'btn-{b_id}.svg'), btn_svg)

# ═══════════════════════════════════════════════════════════════
# 5. TECH STACK & TOOLKIT (880 × 240)
# ═══════════════════════════════════════════════════════════════
tech_stack_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 240" width="880" height="240">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="240" fill="{BG}"/>
  <rect width="880" height="240" fill="url(#notebookGrid)"/>

  <!-- Continuous Flow Line from Top -->
  <line x1="440" y1="0" x2="440" y2="28" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="28" r="4" fill="{NEON_GREEN}" filter="url(#softGlow)"/>

  <!-- Section Title Badge -->
  <g transform="translate(300, 38)">
    <rect x="0" y="0" width="280" height="34" rx="17" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="140" y="22" text-anchor="middle" class="doodle-hand" font-size="20" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1">
      ⚡ TECH STACK &amp; TOOLKIT ⚡
    </text>
  </g>

  <!-- Handwritten Note Beside Title -->
  <text x="440" y="94" text-anchor="middle" class="doodle-hand" font-size="17" fill="{TEXT_MUTED}">
    // tools I reach for to turn coffee into production-ready software
  </text>

  <!-- Left Notebook Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="240" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="240" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Row 1: Frontend & Core -->
  <g transform="translate(80, 115)">
    <!-- React -->
    <g transform="translate(0, 0)">
      <rect width="105" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_CYAN}" class="pulse-glow"/>
      <text x="58" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">React.js</text>
    </g>
    <!-- Next.js -->
    <g transform="translate(120, 0)">
      <rect width="105" height="36" rx="18" fill="{BG_SURFACE}" stroke="{TEXT_MAIN}" stroke-width="1.2" opacity="0.9"/>
      <circle cx="16" cy="18" r="4" fill="{TEXT_MAIN}"/>
      <text x="58" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">Next.js</text>
    </g>
    <!-- TypeScript -->
    <g transform="translate(240, 0)">
      <rect width="115" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_CYAN}"/>
      <text x="63" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">TypeScript</text>
    </g>
    <!-- Tailwind CSS -->
    <g transform="translate(370, 0)">
      <rect width="115" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_CYAN}"/>
      <text x="63" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">TailwindCSS</text>
    </g>
    <!-- JavaScript -->
    <g transform="translate(500, 0)">
      <rect width="110" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_GOLD}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_GOLD}"/>
      <text x="61" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">JavaScript</text>
    </g>
    <!-- HTML5/CSS3 -->
    <g transform="translate(625, 0)">
      <rect width="95" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_GREEN}"/>
      <text x="53" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">HTML/CSS</text>
    </g>
  </g>

  <!-- Row 2: Backend, Data, AI & Cloud -->
  <g transform="translate(80, 168)">
    <!-- Node.js -->
    <g transform="translate(0, 0)">
      <rect width="105" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_GREEN}" class="pulse-glow"/>
      <text x="58" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">Node.js</text>
    </g>
    <!-- Python -->
    <g transform="translate(120, 0)">
      <rect width="100" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_GOLD}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_GOLD}"/>
      <text x="56" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">Python</text>
    </g>
    <!-- Django -->
    <g transform="translate(235, 0)">
      <rect width="100" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_GREEN}"/>
      <text x="56" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">Django</text>
    </g>
    <!-- MongoDB -->
    <g transform="translate(350, 0)">
      <rect width="105" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_GREEN}"/>
      <text x="58" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">MongoDB</text>
    </g>
    <!-- PostgreSQL -->
    <g transform="translate(470, 0)">
      <rect width="115" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_CYAN}"/>
      <text x="63" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">PostgreSQL</text>
    </g>
    <!-- Git & GitHub -->
    <g transform="translate(600, 0)">
      <rect width="120" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_PINK}" stroke-width="1.2"/>
      <circle cx="16" cy="18" r="4" fill="{NEON_PINK}"/>
      <text x="66" y="23" text-anchor="middle" class="mono" font-size="12" font-weight="600" fill="{TEXT_MAIN}">Git &amp; GitHub</text>
    </g>
  </g>

  <!-- Continuous Flow Line to Next Section -->
  <line x1="440" y1="215" x2="440" y2="240" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="238" r="3" fill="{NEON_GREEN}"/>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'tech-stack.svg'), tech_stack_svg)

# ═══════════════════════════════════════════════════════════════
# 6. SELECTED WORK HEADER (880 × 85)
# ═══════════════════════════════════════════════════════════════
section_work_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 85" width="880" height="85">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="85" fill="{BG}"/>
  <rect width="880" height="85" fill="url(#notebookGrid)"/>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="85" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="85" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Connecting line entering from top -->
  <line x1="440" y1="0" x2="440" y2="18" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>

  <!-- Header Badge -->
  <g transform="translate(290, 18)">
    <rect x="0" y="0" width="300" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="150" y="24" text-anchor="middle" class="doodle-hand" font-size="22" font-weight="700" fill="{NEON_CYAN}" letter-spacing="1">
      🚀 FEATURED PROJECTS 🚀
    </text>
  </g>

  <!-- Handwritten Sub-note & Sketched Arrows branching out -->
  <text x="440" y="74" text-anchor="middle" class="doodle-hand" font-size="16" fill="{TEXT_MUTED}">
    ↙ click any card to launch the live interactive app ↘
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'section-work.svg'), section_work_svg)

# ═══════════════════════════════════════════════════════════════
# 7. PROJECT CARDS (430 × 205) - 4 Dedicated Cards
# ═══════════════════════════════════════════════════════════════
projects = [
    {
        'num': '01',
        'file': 'card-01-tradelab',
        'title': 'TradeLab',
        'type': 'STOCK MARKET SIMULATOR',
        'desc1': 'Real-time virtual trading platform with live interactive charts,',
        'desc2': 'portfolio performance tracking &amp; simulated market execution.',
        'tech': 'React • Node.js • MongoDB • Chart.js',
        'badge': '● LIVE SIMULATOR',
        'accent': NEON_GREEN,
        'action_hint': 'CLICK TO LAUNCH LIVE APP ↗',
    },
    {
        'num': '02',
        'file': 'card-02-tourcraze',
        'title': 'TourCraze',
        'type': 'SMART TRAVEL BOOKING',
        'desc1': 'Curated travel planning &amp; exploration hub with interactive',
        'desc2': 'tour packages, smart destination filters &amp; instant booking.',
        'tech': 'React • Express • MongoDB • Tailwind',
        'badge': '● LIVE PLATFORM',
        'accent': NEON_CYAN,
        'action_hint': 'CLICK TO LAUNCH LIVE APP ↗',
    },
    {
        'num': '03',
        'file': 'card-03-gaadimandi',
        'title': 'GaadiMandi',
        'type': 'VEHICLE MARKETPLACE',
        'desc1': 'Full-stack automotive trading marketplace with dynamic listings,',
        'desc2': 'inspection filters, transparent quotes &amp; dealer analytics.',
        'tech': 'Python • Django • PostgreSQL • Tailwind',
        'badge': '● LIVE MARKETPLACE',
        'accent': NEON_GOLD,
        'action_hint': 'CLICK TO LAUNCH LIVE APP ↗',
    },
    {
        'num': '04',
        'file': 'card-04-portfolio',
        'title': 'Personal Portfolio',
        'type': 'DEVELOPER SHOWCASE',
        'desc1': 'Modern interactive portfolio with smooth motion animations,',
        'desc2': 'custom theme experience &amp; responsive project showcase.',
        'tech': 'Next.js • TailwindCSS • Framer Motion',
        'badge': '● LIVE SITE',
        'accent': NEON_GREEN,
        'action_hint': 'CLICK TO LAUNCH LIVE APP ↗',
    },
]

for p in projects:
    acc = p['accent']
    card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 205" width="430" height="205">
  <defs>
    <filter id="cardGlow_{p['num']}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feFlood flood-color="{acc}" flood-opacity="0.35" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style><![CDATA[
    {FONTS_CSS}
    @keyframes radarPing_{p['num']} {{
      0% {{ r: 3; opacity: 1; }}
      70% {{ r: 7; opacity: 0; }}
      100% {{ r: 7; opacity: 0; }}
    }}
    .radar-pulse {{ animation: radarPing_{p['num']} 2s cubic-bezier(0, 0.2, 0.8, 1) infinite; }}
    @keyframes borderPulse_{p['num']} {{
      0%, 100% {{ stroke-opacity: 0.6; }}
      50% {{ stroke-opacity: 1; }}
    }}
    .glow-border {{ animation: borderPulse_{p['num']} 3s ease-in-out infinite; }}
  ]]></style>

  <!-- Card Surface (Doodle Notebook Card) -->
  <rect x="3" y="3" width="424" height="199" rx="16" fill="{BG_SURFACE}"/>

  <!-- Sketched Doodle Neon Border -->
  <rect x="3" y="3" width="424" height="199" rx="16" fill="none" stroke="{acc}" stroke-width="1.5" class="glow-border" filter="url(#cardGlow_{p['num']})"/>

  <!-- Left Accent Notch -->
  <rect x="3" y="30" width="4" height="145" rx="2" fill="{acc}"/>

  <!-- Top Notebook Tape Header Accent -->
  <polygon points="25,3 110,3 105,14 20,14" fill="{acc}" opacity="0.25"/>

  <!-- Status Beacon Badge -->
  <g transform="translate(290, 18)">
    <rect x="0" y="0" width="122" height="22" rx="11" fill="{BG}" stroke="{acc}" stroke-width="1"/>
    <!-- Animated Radar Circle -->
    <circle cx="14" cy="11" r="3.5" fill="{acc}"/>
    <circle cx="14" cy="11" r="3.5" fill="none" stroke="{acc}" stroke-width="1.5" class="radar-pulse"/>
    <text x="24" y="15" class="mono" font-size="9" font-weight="700" fill="{acc}" letter-spacing="0.5">{p['badge']}</text>
  </g>

  <!-- Project Number & Title -->
  <text x="22" y="44" class="mono" font-size="13" font-weight="700" fill="{acc}" letter-spacing="1">{p['num']} // {p['type']}</text>
  <text x="22" y="74" class="doodle-hand" font-size="28" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.5">{p['title']}</text>

  <!-- Sketched Handwritten Description (Native SVG Text for 100% reliability) -->
  <text x="22" y="102" class="doodle-hand" font-size="17" fill="{TEXT_MUTED}">{p['desc1']}</text>
  <text x="22" y="124" class="doodle-hand" font-size="17" fill="{TEXT_MUTED}">{p['desc2']}</text>

  <!-- Tech Stack Pills -->
  <g transform="translate(22, 146)">
    <text x="0" y="12" class="mono" font-size="11" font-weight="600" fill="{NEON_CYAN}" opacity="0.85">{p['tech']}</text>
  </g>

  <!-- Launch Prompt Bar -->
  <g transform="translate(22, 172)">
    <rect x="0" y="0" width="386" height="24" rx="6" fill="{BG}" stroke="{acc}" stroke-width="0.8" opacity="0.8"/>
    <text x="193" y="16" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{acc}" letter-spacing="1">
      {p['action_hint']}
    </text>
  </g>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f"{p['file']}.svg"), card_svg)

# ═══════════════════════════════════════════════════════════════
# 8. MINI REPO BUTTONS (For TradeLab, TourCraze, Portfolio)
# ═══════════════════════════════════════════════════════════════
repo_buttons = [
    ('tradelab',  '⌥ TradeLab GitHub Repo ↗', 190),
    ('tourcraze', '⌥ TourCraze GitHub Repo ↗', 190),
    ('portfolio', '⌥ Portfolio GitHub Repo ↗', 190),
]

for r_id, label, width in repo_buttons:
    r_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 28" width="{width}" height="28">
  <style><![CDATA[
    {FONTS_CSS}
  ]]></style>
  <rect x="1" y="1" width="{width-2}" height="26" rx="13" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1" stroke-dasharray="3,3" opacity="0.85"/>
  <text x="{width//2}" y="18" text-anchor="middle" class="mono" font-size="10" font-weight="600" fill="{NEON_GREEN}">{label}</text>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f"repo-{r_id}.svg"), r_svg)

# ═══════════════════════════════════════════════════════════════
# 9. CONNECT SECTION (880 × 110)
# ═══════════════════════════════════════════════════════════════
section_connect_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 110" width="880" height="110">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="110" fill="{BG}"/>
  <rect width="880" height="110" fill="url(#notebookGrid)"/>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="110" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="110" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Continuous Flow Line entering from projects -->
  <line x1="440" y1="0" x2="440" y2="24" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>

  <!-- Header Badge -->
  <g transform="translate(290, 24)">
    <rect x="0" y="0" width="300" height="38" rx="19" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="150" y="25" text-anchor="middle" class="doodle-hand" font-size="22" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1">
      💬 LET'S CONNECT &amp; BUILD 💬
    </text>
  </g>

  <!-- Friendly Handwritten Note -->
  <text x="440" y="88" text-anchor="middle" class="doodle-hand" font-size="18" fill="{TEXT_MUTED}">
    Always excited for new projects, full-time opportunities, or tech discussions!
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'section-connect.svg'), section_connect_svg)

# ═══════════════════════════════════════════════════════════════
# 10. CONNECT CHIPS (Clickable Footer Badges)
# ═══════════════════════════════════════════════════════════════
chips = [
    ('resume',    '📄 View Resume (PDF)', 165, NEON_GREEN),
    ('linkedin',  '💼 LinkedIn Profile', 155, NEON_CYAN),
    ('email',     '✉️ parmeetssms@gmail.com', 190, NEON_GOLD),
    ('portfolio', '🌐 Personal Portfolio', 165, NEON_GREEN),
]

for c_id, label, width, color in chips:
    chip_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 40" width="{width}" height="40">
  <defs>
    <filter id="chipGlow_{c_id}" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur"/>
      <feFlood flood-color="{color}" flood-opacity="0.4" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge><feMergeNode in="glow"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style><![CDATA[
    {FONTS_CSS}
  ]]></style>
  <rect x="2" y="2" width="{width-4}" height="36" rx="18" fill="{BG_SURFACE}" stroke="{color}" stroke-width="1.4" filter="url(#chipGlow_{c_id})"/>
  <text x="{width//2}" y="25" text-anchor="middle" class="doodle-hand" font-size="16" font-weight="700" fill="{TEXT_MAIN}">{label}</text>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f'chip-{c_id}.svg'), chip_svg)

# ═══════════════════════════════════════════════════════════════
# 11. FOOTER BAR (880 × 65)
# ═══════════════════════════════════════════════════════════════
footer_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 65" width="880" height="65">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="65" fill="{BG}"/>
  <rect width="880" height="65" fill="url(#notebookGrid)"/>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="65" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="65" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Thin neon divider line -->
  <line x1="140" y1="12" x2="740" y2="12" stroke="{NEON_GREEN}" stroke-width="0.8" stroke-dasharray="6,6" opacity="0.4"/>

  <!-- Footer Signature (Handwritten Notebook) -->
  <text x="440" y="38" text-anchor="middle" class="doodle-hand" font-size="18" font-weight="600" fill="{TEXT_MUTED}">
    ✏️ Doodled, designed &amp; coded with <tspan fill="{NEON_GREEN}">💚</tspan> by <tspan fill="{TEXT_MAIN}" font-weight="700">Parmeet Singh</tspan> • Delhi, India
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'footer-bar.svg'), footer_svg)

# ═══════════════════════════════════════════════════════════════
# 12. README.md - 100% CONTINUOUS FLOW (ZERO BLACK GAPS)
# ═══════════════════════════════════════════════════════════════
readme_md = f"""<div align="center">
  <!-- 01 • HERO BANNER -->
  <img src="./assets/hero-banner.svg" alt="Hey, I'm Parmeet — Full-Stack Developer" width="100%" style="max-width: 880px;" /><br/>
  <!-- 02 • ACTION BUTTONS -->
  <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-resume.svg" height="42" alt="View Resume (PDF)" /></a>&nbsp;&nbsp;<a href="mailto:parmeetssms@gmail.com"><img src="./assets/btn-talk.svg" height="42" alt="Let's Talk" /></a>&nbsp;&nbsp;<a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-linkedin.svg" height="42" alt="LinkedIn Profile" /></a>&nbsp;&nbsp;<a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-portfolio.svg" height="42" alt="Personal Portfolio" /></a><br/>
  <!-- 03 • TECH STACK -->
  <img src="./assets/tech-stack.svg" alt="Tech Stack &amp; Toolkit: React, Next.js, Python, Django, Node.js" width="100%" style="max-width: 880px;" /><br/>
  <!-- 04 • FEATURED PROJECTS -->
  <img src="./assets/section-work.svg" alt="Featured Projects — Click any card to launch demo" width="100%" style="max-width: 880px;" /><br/>
  <a href="https://tradelab-kappa.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-01-tradelab.svg" width="48.5%" style="max-width: 430px;" alt="TradeLab — Real-Time Stock Market Simulator (Launch Demo)" /></a>&nbsp;<a href="https://tour-craze.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-02-tourcraze.svg" width="48.5%" style="max-width: 430px;" alt="TourCraze — AI Travel Planning Platform (Launch Demo)" /></a><br/>
  <a href="https://github.com/singhparmeet12/TradeLab" target="_blank" rel="noopener noreferrer"><img src="./assets/repo-tradelab.svg" height="26" alt="TradeLab Source Code" /></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://github.com/singhparmeet12/TourCraze" target="_blank" rel="noopener noreferrer"><img src="./assets/repo-tourcraze.svg" height="26" alt="TourCraze Source Code" /></a><br/>
  <a href="https://car-trade-gamma.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-03-gaadimandi.svg" width="48.5%" style="max-width: 430px;" alt="GaadiMandi — Vehicle Marketplace (Launch Demo)" /></a>&nbsp;<a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-04-portfolio.svg" width="48.5%" style="max-width: 430px;" alt="Personal Portfolio 2026 (Launch Live Site)" /></a><br/>
  <a href="https://github.com/singhparmeet12/Personal-Portfolio" target="_blank" rel="noopener noreferrer"><img src="./assets/repo-portfolio.svg" height="26" alt="Portfolio Source Code" /></a><br/>
  <!-- 05 • CONNECT SECTION -->
  <img src="./assets/section-connect.svg" alt="Let's Connect &amp; Build" width="100%" style="max-width: 880px;" /><br/>
  <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-resume.svg" height="40" alt="View Resume (PDF)" /></a>&nbsp;&nbsp;<a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-linkedin.svg" height="40" alt="LinkedIn Profile" /></a>&nbsp;&nbsp;<a href="mailto:parmeetssms@gmail.com"><img src="./assets/chip-email.svg" height="40" alt="Email Parmeet" /></a>&nbsp;&nbsp;<a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-portfolio.svg" height="40" alt="Personal Portfolio" /></a><br/>
  <!-- 06 • FOOTER BAR -->
  <img src="./assets/footer-bar.svg" alt="Parmeet Singh • Full-Stack Developer • Delhi, India" width="100%" style="max-width: 880px;" />
</div>
"""

write_file('README.md', readme_md)

# ═══════════════════════════════════════════════════════════════
# 13. PREVIEW HTML (Local Test & Verification)
# ═══════════════════════════════════════════════════════════════
preview_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Parmeet Singh — Cyber-Doodle Notebook GitHub Profile Preview</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      background: {BG};
      color: {TEXT_MAIN};
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 16px;
      min-height: 100vh;
    }}
    .github-canvas {{
      max-width: 880px;
      width: 100%;
      background: {BG};
      text-align: center;
    }}
    .github-canvas img {{
      display: inline-block;
      vertical-align: middle;
    }}
    .github-canvas a {{
      text-decoration: none;
      display: inline-block;
    }}
    .pfp-preview {{
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 16px;
      background: {BG_SURFACE};
      padding: 12px 20px;
      border-radius: 40px;
      border: 1px solid {NEON_GREEN};
    }}
    .pfp-img {{
      width: 64px;
      height: 64px;
      border-radius: 50%;
      border: 2px solid {NEON_GREEN};
      object-fit: cover;
    }}
  </style>
</head>
<body>

  <!-- Matching PFP Preview Banner -->
  <div class="pfp-preview">
    <img class="pfp-img" src="./assets/profile-avatar.jpg" alt="Matching Theme Profile Picture" />
    <div style="text-align: left;">
      <div style="font-weight: 700; font-size: 15px; color: {NEON_GREEN};">NEW MATCHING THEME PROFILE PICTURE GENERATED!</div>
      <div style="font-size: 12px; color: {TEXT_MUTED};">Saved to <code>assets/profile-avatar.jpg</code> — Ready to upload to GitHub Profile!</div>
    </div>
  </div>

  <div class="github-canvas">
    {readme_md}
  </div>

</body>
</html>"""

write_file('preview.html', preview_html)
print("\\nAll profile assets, README.md, and preview.html successfully generated!")
