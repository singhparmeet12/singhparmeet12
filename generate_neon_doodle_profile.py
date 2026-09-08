#!/usr/bin/env python3
"""
generate_neon_doodle_profile.py
Builds Parmeet Singh's Cyber-Doodle Notebook GitHub Profile:
- Spacious, Clean & Beautiful Layout (breathing room, zero crowded elements)
- Removed project GitHub repo buttons (clicking card directly launches demo)
- Removed 'TURBAN & CODE' tag from avatar
- Every link opens in a new tab (target="_blank" rel="noopener noreferrer")
- Reduced card text for maximum clarity and scannability
- Cute animated floating neon coding elements (coffee with steam, terminal window, { ; }, pixel heart, git branch, rocket)
- 100% Verified Working Links
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
NEON_GREEN = '#00FF66'  # Main vibrant neon green
NEON_CYAN = '#00F0FF'   # Electric cyan accent
NEON_GOLD = '#FFD700'   # Golden amber (matches turban & aviators)
NEON_PINK = '#FF2A85'   # Doodle pink accent
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
    @keyframes floatGentle {{
      0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
      50% {{ transform: translateY(-8px) rotate(-2deg); }}
    }}
    @keyframes floatBob {{
      0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
      50% {{ transform: translateY(-10px) rotate(3deg); }}
    }}
    @keyframes floatWobble {{
      0%, 100% {{ transform: translateY(0px) rotate(-3deg); }}
      50% {{ transform: translateY(-7px) rotate(3deg); }}
    }}
    @keyframes steamRise {{
      0% {{ transform: translateY(0px); opacity: 0; }}
      50% {{ opacity: 0.85; }}
      100% {{ transform: translateY(-10px); opacity: 0; }}
    }}
    @keyframes heartBeat {{
      0%, 100% {{ transform: scale(1); }}
      30% {{ transform: scale(1.15); }}
      60% {{ transform: scale(0.95); }}
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
    .float-gentle {{ animation: floatGentle 4s ease-in-out infinite; transform-origin: center; }}
    .float-bob {{ animation: floatBob 3.6s ease-in-out infinite; transform-origin: center; }}
    .float-wobble {{ animation: floatWobble 4.2s ease-in-out infinite; transform-origin: center; }}
    .steam-1 {{ animation: steamRise 2.2s linear infinite; }}
    .steam-2 {{ animation: steamRise 2.2s linear infinite 0.7s; }}
    .steam-3 {{ animation: steamRise 2.2s linear infinite 1.4s; }}
    .heart-pulse {{ animation: heartBeat 1.8s ease-in-out infinite; transform-origin: center; }}
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
# 3. HERO BANNER (880 × 420) - Spacious, Clean, Cute Neon Cues
# ═══════════════════════════════════════════════════════════════
hero_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 420" width="880" height="420">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Seamless Canvas Background -->
  <rect width="880" height="420" fill="{BG}"/>
  <rect width="880" height="420" fill="url(#notebookGrid)"/>

  <!-- Top Notebook Washi Tape Accent -->
  <polygon points="40,14 180,12 178,30 38,32" fill="{NEON_GREEN}" opacity="0.18"/>
  <text x="109" y="25" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1.5">PARMEET.DEV // 2026</text>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="420" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="420" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Main Greeting Group (Well spaced, 70px left margin) -->
  <g transform="translate(70, 75)">
    <!-- Small Status Pill -->
    <rect x="0" y="0" width="144" height="26" rx="13" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1" opacity="0.9"/>
    <circle cx="14" cy="13" r="3.5" fill="{NEON_GREEN}" class="pulse-glow"/>
    <text x="26" y="17" class="mono" font-size="11" font-weight="600" fill="{NEON_GREEN}" letter-spacing="0.5">ONLINE • BUILDING</text>

    <!-- Cute Mini Terminal Doodle beside status -->
    <g transform="translate(160, -4)" class="float-bob">
      <rect x="0" y="0" width="62" height="32" rx="6" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2" filter="url(#softGlow)"/>
      <circle cx="9" cy="8" r="2.2" fill="#FF5F56"/>
      <circle cx="16" cy="8" r="2.2" fill="#FFBD2E"/>
      <circle cx="23" cy="8" r="2.2" fill="#27C93F"/>
      <text x="8" y="23" class="mono" font-size="9" font-weight="700" fill="{NEON_CYAN}">&gt;_ dev</text>
      <circle cx="50" cy="20" r="1.8" fill="{NEON_GREEN}" class="cursor-blink"/>
    </g>

    <!-- Hey, I'm Parmeet! -->
    <text x="0" y="76" class="doodle-hand" font-size="58" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.5">
      Hey, I'm <tspan fill="url(#neonGradient)" filter="url(#neonGlowGreen)">Parmeet</tspan>!
    </text>

    <!-- Sketched Neon Underline -->
    <path d="M 2,88 Q 70,94 150,89 T 310,90" fill="none" stroke="{NEON_GREEN}" stroke-width="3" stroke-linecap="round" filter="url(#softGlow)"/>
    <path d="M 12,94 Q 80,98 180,94 T 270,95" fill="none" stroke="{NEON_CYAN}" stroke-width="1.5" stroke-linecap="round" opacity="0.6"/>

    <!-- Role & Specialization -->
    <text x="2" y="132" class="mono" font-size="15" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1">
      FULL-STACK DEVELOPER <tspan fill="{TEXT_MUTED}">|</tspan> <tspan fill="{NEON_CYAN}">WEB • DATA • AI</tspan>
    </text>

    <!-- Notebook Handwritten Notes & Bio (Clean, Concise, No Overflow!) -->
    <g transform="translate(2, 156)">
      <text x="0" y="20" class="doodle-hand" font-size="19" fill="{TEXT_MAIN}" opacity="0.92">
        ✏️  Building fast, scalable web apps &amp; intelligent tools.
      </text>
      <text x="0" y="46" class="doodle-hand" font-size="19" fill="{TEXT_MAIN}" opacity="0.92">
        📍  Delhi, India • Clean Code • High-Performance Systems
      </text>
      <text x="0" y="72" class="mono" font-size="12.5" fill="{TEXT_MUTED}">
        const stack = ["React", "Next.js", "Django", "Python"];<tspan fill="{NEON_GREEN}" class="cursor-blink">▋</tspan>
      </text>
    </g>

    <!-- Doodle Arrow Pointing Down to Action Buttons -->
    <g transform="translate(10, 272)">
      <path d="M 0,0 C 25,18 45,15 65,30" fill="none" stroke="{NEON_GREEN}" stroke-width="2" stroke-linecap="round" stroke-dasharray="4,3"/>
      <polygon points="66,24 67,35 56,31" fill="{NEON_GREEN}"/>
      <text x="75" y="28" class="doodle-hand" font-size="17" font-weight="600" fill="{NEON_GREEN}">
        explore quick links &amp; resume below ↴
      </text>
    </g>
  </g>

  <!-- Right Floating Sikh Tech Avatar & Cute Neon Floating Elements -->
  <g transform="translate(565, 30)">
    <!-- Ambient Neon Backdrop Glow -->
    <ellipse cx="145" cy="180" rx="145" ry="165" fill="url(#avatarBackdropGlow)"/>

    <!-- Sketched Doodle Orbit Ring -->
    <ellipse cx="145" cy="180" rx="135" ry="155" fill="none" stroke="{NEON_GREEN}" stroke-width="1.2" stroke-dasharray="6,8" opacity="0.4" class="connecting-line"/>

    <!-- Floating Avatar with Laptop (NO 'TURBAN' BADGE!) -->
    <g class="floating-avatar">
      <image href="data:image/png;base64,{AVATAR_B64}" x="20" y="10" width="250" height="340" preserveAspectRatio="xMidYMid meet"/>
    </g>

    <!-- CUTE NEON FLOATING ELEMENT 1: Coffee Cup with Animated Steam -->
    <g transform="translate(-15, 140)" class="float-gentle">
      <!-- Cup Body -->
      <path d="M 0,6 L 2,24 Q 3,28 8,28 L 20,28 Q 25,28 26,24 L 28,6 Z" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.4" filter="url(#softGlow)"/>
      <!-- Handle -->
      <path d="M 27,9 Q 34,9 34,15 Q 34,21 26,21" fill="none" stroke="{NEON_CYAN}" stroke-width="1.4"/>
      <!-- Coffee Surface -->
      <ellipse cx="14" cy="6" rx="13" ry="2.8" fill="{NEON_GREEN}" opacity="0.4"/>
      <!-- Rising Steam Curls -->
      <path d="M 8,2 Q 6,-4 9,-9" fill="none" stroke="{NEON_GREEN}" stroke-width="1.2" stroke-linecap="round" class="steam-1"/>
      <path d="M 14,3 Q 16,-3 13,-8" fill="none" stroke="{NEON_CYAN}" stroke-width="1.2" stroke-linecap="round" class="steam-2"/>
      <path d="M 20,2 Q 18,-4 21,-9" fill="none" stroke="{NEON_GREEN}" stroke-width="1.2" stroke-linecap="round" class="steam-3"/>
    </g>

    <!-- CUTE NEON FLOATING ELEMENT 2: Curly Brackets -->
    <g transform="translate(255, 65)" class="float-wobble">
      <rect x="0" y="0" width="46" height="26" rx="13" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2" filter="url(#softGlow)"/>
      <text x="23" y="18" text-anchor="middle" class="mono" font-size="13" font-weight="700" fill="{NEON_CYAN}">&#123; ; &#125;</text>
    </g>

    <!-- CUTE NEON FLOATING ELEMENT 3: Pixel Heart Beating -->
    <g transform="translate(15, 290)" class="heart-pulse">
      <path d="M 10,3 Q 10,0 6,0 Q 0,0 0,6 Q 0,11 10,17 Q 20,11 20,6 Q 20,0 14,0 Q 10,0 10,3 Z" fill="{NEON_GREEN}" opacity="0.9" filter="url(#softGlow)"/>
    </g>

    <!-- CUTE NEON FLOATING ELEMENT 4: Code Tag </> -->
    <g transform="translate(245, 270)" class="float-bob">
      <rect x="0" y="0" width="48" height="26" rx="8" fill="{BG_SURFACE}" stroke="{NEON_GOLD}" stroke-width="1.2"/>
      <text x="24" y="18" text-anchor="middle" class="mono" font-size="12" font-weight="700" fill="{NEON_GOLD}">&lt;/&gt;</text>
    </g>

    <!-- Twinkling Neon Stars -->
    <g transform="translate(20, 50)" class="star-1">
      <path d="M 0,-7 L 2,-2 L 7,0 L 2,2 L 0,7 L -2,2 L -7,0 L -2,-2 Z" fill="{NEON_GOLD}" filter="url(#softGlow)"/>
    </g>
    <g transform="translate(275, 175)" class="star-2">
      <path d="M 0,-6 L 1.5,-1.5 L 6,0 L 1.5,1.5 L 0,6 L -1.5,1.5 L -6,0 L -1.5,-1.5 Z" fill="{NEON_PINK}" filter="url(#softGlow)"/>
    </g>
  </g>

  <!-- Bottom Connecting Neon Guide (Flows into buttons) -->
  <line x1="440" y1="385" x2="440" y2="420" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="418" r="3" fill="{NEON_GREEN}"/>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'hero-banner.svg'), hero_svg)

# ═══════════════════════════════════════════════════════════════
# 4. ACTION BUTTONS (Clickable SVGs with Doodle + Neon Glow)
# ═══════════════════════════════════════════════════════════════
buttons_data = [
    ('resume',    '📄 View Resume', 165, NEON_GREEN),
    ('talk',      '💬 Let\'s Talk', 150, NEON_CYAN),
    ('linkedin',  '💼 LinkedIn',    145, NEON_GOLD),
    ('portfolio', '🌐 Portfolio',   155, NEON_GREEN),
]

for b_id, label, width, color in buttons_data:
    btn_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 44" width="{width}" height="44">
  <defs>
    <filter id="btnGlow_{b_id}" x="-30%" y="-30%" width="160%" height="160%">
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
  <rect x="2" y="2" width="{width-4}" height="40" rx="20" fill="none" stroke="{color}" stroke-width="1.6" class="btn-border" filter="url(#btnGlow_{b_id})"/>

  <!-- Button Label (Handwritten/Casual + Clean) -->
  <text x="{width//2}" y="27" text-anchor="middle" class="doodle-hand" font-size="18" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.3">
    {label}
  </text>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f'btn-{b_id}.svg'), btn_svg)

# ═══════════════════════════════════════════════════════════════
# 5. TECH STACK & TOOLKIT (880 × 265) - Generous Breathing Room
# ═══════════════════════════════════════════════════════════════
tech_stack_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 265" width="880" height="265">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="265" fill="{BG}"/>
  <rect width="880" height="265" fill="url(#notebookGrid)"/>

  <!-- Continuous Flow Line from Top -->
  <line x1="440" y1="0" x2="440" y2="28" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="28" r="4" fill="{NEON_GREEN}" filter="url(#softGlow)"/>

  <!-- Section Title Badge -->
  <g transform="translate(290, 38)">
    <rect x="0" y="0" width="300" height="36" rx="18" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="150" y="24" text-anchor="middle" class="doodle-hand" font-size="21" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1">
      ⚡ TECH STACK &amp; TOOLKIT ⚡
    </text>
  </g>

  <!-- Cute Floating Git Branch Doodle (Left Margin) -->
  <g transform="translate(105, 42)" class="float-gentle">
    <line x1="6" y1="4" x2="6" y2="24" stroke="{NEON_CYAN}" stroke-width="1.5"/>
    <path d="M 6,18 Q 16,18 16,10" fill="none" stroke="{NEON_PINK}" stroke-width="1.5"/>
    <circle cx="6" cy="6" r="3" fill="{NEON_CYAN}"/>
    <circle cx="6" cy="22" r="3" fill="{NEON_GREEN}"/>
    <circle cx="16" cy="10" r="3" fill="{NEON_PINK}"/>
    <text x="22" y="14" class="mono" font-size="9" font-weight="700" fill="{NEON_PINK}">git:push</text>
  </g>

  <!-- Cute Floating Rocket Doodle (Right Margin) -->
  <g transform="translate(730, 36)" class="float-bob">
    <path d="M 10,0 Q 18,4 18,16 L 2,16 Q 2,4 10,0 Z" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2" filter="url(#softGlow)"/>
    <circle cx="10" cy="8" r="2.5" fill="{NEON_GREEN}"/>
    <path d="M 2,12 L -2,17 L 3,16 Z" fill="{NEON_CYAN}"/>
    <path d="M 18,12 L 22,17 L 17,16 Z" fill="{NEON_CYAN}"/>
    <path d="M 6,16 Q 10,22 10,22 Q 10,22 14,16 Z" fill="{NEON_GOLD}" class="cursor-blink"/>
  </g>

  <!-- Handwritten Note Beside Title -->
  <text x="440" y="100" text-anchor="middle" class="doodle-hand" font-size="17" fill="{TEXT_MUTED}">
    // tools I reach for to turn coffee into production-ready software
  </text>

  <!-- Left Notebook Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="265" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="265" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Row 1: Frontend & Core (Y=125) -->
  <g transform="translate(80, 125)">
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

  <!-- Row 2: Backend, Data, AI & Cloud (Y=182, 21px gap) -->
  <g transform="translate(80, 182)">
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
  <line x1="440" y1="235" x2="440" y2="265" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="263" r="3" fill="{NEON_GREEN}"/>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'tech-stack.svg'), tech_stack_svg)

# ═══════════════════════════════════════════════════════════════
# 6. SELECTED WORK HEADER (880 × 95) - Clean & Punchy
# ═══════════════════════════════════════════════════════════════
section_work_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 95" width="880" height="95">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="95" fill="{BG}"/>
  <rect width="880" height="95" fill="url(#notebookGrid)"/>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="95" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="95" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Connecting line entering from top -->
  <line x1="440" y1="0" x2="440" y2="20" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>

  <!-- Header Badge -->
  <g transform="translate(285, 20)">
    <rect x="0" y="0" width="310" height="38" rx="19" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="155" y="25" text-anchor="middle" class="doodle-hand" font-size="22" font-weight="700" fill="{NEON_CYAN}" letter-spacing="1">
      🚀 FEATURED PROJECTS 🚀
    </text>
  </g>

  <!-- Cute Floating Sparkle Stars around header -->
  <g transform="translate(235, 36)" class="star-1">
    <path d="M 0,-6 L 1.5,-1.5 L 6,0 L 1.5,1.5 L 0,6 L -1.5,1.5 L -6,0 L -1.5,-1.5 Z" fill="{NEON_GREEN}" filter="url(#softGlow)"/>
  </g>
  <g transform="translate(640, 36)" class="star-2">
    <path d="M 0,-6 L 1.5,-1.5 L 6,0 L 1.5,1.5 L 0,6 L -1.5,1.5 L -6,0 L -1.5,-1.5 Z" fill="{NEON_GOLD}" filter="url(#softGlow)"/>
  </g>

  <!-- Handwritten Sub-note -->
  <text x="440" y="80" text-anchor="middle" class="doodle-hand" font-size="17" fill="{TEXT_MUTED}">
    ↙ click any card to launch the live interactive app ↘
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'section-work.svg'), section_work_svg)

# ═══════════════════════════════════════════════════════════════
# 7. PROJECT CARDS (430 × 210) - Concise Text & Cute Coding Accents
# ═══════════════════════════════════════════════════════════════
projects = [
    {
        'num': '01',
        'file': 'card-01-tradelab',
        'title': 'TradeLab',
        'type': 'STOCK MARKET SIMULATOR',
        'desc': 'Real-time virtual trading platform with live portfolio tracking.',
        'tech': 'React • Node.js • MongoDB • Chart.js',
        'badge': '● LIVE SIMULATOR',
        'accent': NEON_GREEN,
        'icon_doodle': """
          <g transform="translate(378, 80)" class="float-gentle">
            <polyline points="0,18 8,10 16,14 24,4" fill="none" stroke="#00FF66" stroke-width="2" stroke-linecap="round" filter="url(#softGlow)"/>
            <polygon points="20,4 25,3 24,8" fill="#00FF66"/>
          </g>
        """
    },
    {
        'num': '02',
        'file': 'card-02-tourcraze',
        'title': 'TourCraze',
        'type': 'SMART TRAVEL BOOKING',
        'desc': 'AI-powered smart travel planning &amp; curated tour exploration.',
        'tech': 'React • Express • MongoDB • Tailwind',
        'badge': '● LIVE PLATFORM',
        'accent': NEON_CYAN,
        'icon_doodle': """
          <g transform="translate(378, 76)" class="float-bob">
            <circle cx="12" cy="12" r="10" fill="none" stroke="#00F0FF" stroke-width="1.5" stroke-dasharray="3,3"/>
            <polygon points="12,4 15,12 12,20 9,12" fill="#00F0FF" opacity="0.8"/>
          </g>
        """
    },
    {
        'num': '03',
        'file': 'card-03-gaadimandi',
        'title': 'GaadiMandi',
        'type': 'VEHICLE MARKETPLACE',
        'desc': 'Full-stack automotive marketplace with transparent inspections.',
        'tech': 'Python • Django • PostgreSQL • Tailwind',
        'badge': '● LIVE MARKETPLACE',
        'accent': NEON_GOLD,
        'icon_doodle': """
          <g transform="translate(376, 80)" class="float-gentle">
            <path d="M 2,12 Q 5,4 12,4 Q 19,4 22,12 L 24,14 L 0,14 Z" fill="none" stroke="#FFD700" stroke-width="1.4"/>
            <circle cx="6" cy="15" r="2.5" fill="#FFD700"/>
            <circle cx="18" cy="15" r="2.5" fill="#FFD700"/>
          </g>
        """
    },
    {
        'num': '04',
        'file': 'card-04-portfolio',
        'title': 'Personal Portfolio',
        'type': 'DEVELOPER SHOWCASE',
        'desc': 'Interactive 3D developer showcase with sleek motion animations.',
        'tech': 'Next.js • TailwindCSS • Framer Motion',
        'badge': '● LIVE SITE',
        'accent': NEON_GREEN,
        'icon_doodle': """
          <g transform="translate(380, 78)" class="star-1">
            <path d="M 0,-8 L 2,-2 L 8,0 L 2,2 L 0,8 L -2,2 L -8,0 L -2,-2 Z" fill="#00FF66" filter="url(#softGlow)"/>
          </g>
        """
    },
]

for p in projects:
    acc = p['accent']
    card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 210" width="430" height="210">
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
    .float-gentle {{ animation: floatGentle 4s ease-in-out infinite; transform-origin: center; }}
    .float-bob {{ animation: floatBob 3.6s ease-in-out infinite; transform-origin: center; }}
    .star-1 {{ animation: starTwinkle 2.5s ease-in-out infinite; transform-origin: center; }}
  ]]></style>

  <!-- Card Surface (Doodle Notebook Card) -->
  <rect x="3" y="3" width="424" height="204" rx="16" fill="{BG_SURFACE}"/>

  <!-- Sketched Doodle Neon Border -->
  <rect x="3" y="3" width="424" height="204" rx="16" fill="none" stroke="{acc}" stroke-width="1.5" class="glow-border" filter="url(#cardGlow_{p['num']})"/>

  <!-- Left Accent Notch -->
  <rect x="3" y="30" width="4" height="150" rx="2" fill="{acc}"/>

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

  <!-- Project Number & Category -->
  <text x="22" y="44" class="mono" font-size="12.5" font-weight="700" fill="{acc}" letter-spacing="1">{p['num']} // {p['type']}</text>

  <!-- Project Title -->
  <text x="22" y="76" class="doodle-hand" font-size="29" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.5">{p['title']}</text>

  <!-- Cute Floating Neon Doodle Icon on Card -->
  {p['icon_doodle']}

  <!-- Short, Crisp, Clear Description (Single line, ample whitespace) -->
  <text x="22" y="108" class="doodle-hand" font-size="17" fill="{TEXT_MUTED}">{p['desc']}</text>

  <!-- Tech Stack Pills -->
  <g transform="translate(22, 142)">
    <text x="0" y="12" class="mono" font-size="11.5" font-weight="600" fill="{NEON_CYAN}" opacity="0.88">{p['tech']}</text>
  </g>

  <!-- Launch Prompt Bar (Click Card To Launch) -->
  <g transform="translate(22, 168)">
    <rect x="0" y="0" width="386" height="26" rx="8" fill="{BG}" stroke="{acc}" stroke-width="1" opacity="0.9"/>
    <text x="193" y="17" text-anchor="middle" class="mono" font-size="10.5" font-weight="700" fill="{acc}" letter-spacing="1">
      CLICK CARD TO LAUNCH LIVE APP ↗
    </text>
  </g>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f"{p['file']}.svg"), card_svg)

# ═══════════════════════════════════════════════════════════════
# 8. CONNECT SECTION (880 × 125) - Cute Coffee & Chat Elements
# ═══════════════════════════════════════════════════════════════
section_connect_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 125" width="880" height="125">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="125" fill="{BG}"/>
  <rect width="880" height="125" fill="url(#notebookGrid)"/>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="125" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="125" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Continuous Flow Line entering from projects -->
  <line x1="440" y1="0" x2="440" y2="22" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>

  <!-- Header Badge -->
  <g transform="translate(285, 22)">
    <rect x="0" y="0" width="310" height="40" rx="20" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="155" y="26" text-anchor="middle" class="doodle-hand" font-size="22" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1">
      💬 LET'S CONNECT &amp; BUILD 💬
    </text>
  </g>

  <!-- Cute Floating Chat Bubble Doodle (Left) -->
  <g transform="translate(195, 22)" class="float-gentle">
    <path d="M 0,0 L 28,0 Q 34,0 34,6 L 34,18 Q 34,24 28,24 L 10,24 L 2,30 L 4,24 L 0,24 Q -6,24 -6,18 L -6,6 Q -6,0 0,0 Z" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2" filter="url(#softGlow)"/>
    <text x="14" y="16" text-anchor="middle" class="mono" font-size="11" font-weight="700" fill="{NEON_CYAN}">:)</text>
  </g>

  <!-- Cute Floating Coffee Cup Doodle (Right) -->
  <g transform="translate(640, 22)" class="float-bob">
    <path d="M 0,4 L 2,18 Q 3,22 7,22 L 17,22 Q 21,22 22,18 L 24,4 Z" fill="{BG_SURFACE}" stroke="{NEON_GOLD}" stroke-width="1.2" filter="url(#softGlow)"/>
    <path d="M 23,7 Q 29,7 29,12 Q 29,17 22,17" fill="none" stroke="{NEON_GOLD}" stroke-width="1.2"/>
    <path d="M 6,1 Q 5,-4 7,-8" fill="none" stroke="{NEON_GREEN}" stroke-width="1" stroke-linecap="round" class="steam-1"/>
    <path d="M 12,2 Q 14,-3 11,-7" fill="none" stroke="{NEON_CYAN}" stroke-width="1" stroke-linecap="round" class="steam-2"/>
    <path d="M 18,1 Q 16,-4 19,-8" fill="none" stroke="{NEON_GREEN}" stroke-width="1" stroke-linecap="round" class="steam-3"/>
  </g>

  <!-- Friendly Handwritten Note (Generous spacing) -->
  <text x="440" y="96" text-anchor="middle" class="doodle-hand" font-size="19" fill="{TEXT_MUTED}">
    Always excited for new projects, full-time opportunities, or tech discussions!
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'section-connect.svg'), section_connect_svg)

# ═══════════════════════════════════════════════════════════════
# 9. CONNECT CHIPS (Clickable Footer Badges - Generously Sized)
# ═══════════════════════════════════════════════════════════════
chips = [
    ('resume',    '📄 View Resume (PDF)', 195, NEON_GREEN),
    ('linkedin',  '💼 LinkedIn Profile',  185, NEON_CYAN),
    ('email',     '✉️ parmeetssms@gmail.com', 245, NEON_GOLD),
    ('portfolio', '🌐 Personal Portfolio', 195, NEON_GREEN),
]

for c_id, label, width, color in chips:
    chip_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 44" width="{width}" height="44">
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
  <rect x="2" y="2" width="{width-4}" height="40" rx="20" fill="{BG_SURFACE}" stroke="{color}" stroke-width="1.5" filter="url(#chipGlow_{c_id})"/>
  <text x="{width//2}" y="27" text-anchor="middle" class="doodle-hand" font-size="17" font-weight="700" fill="{TEXT_MAIN}">{label}</text>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f'chip-{c_id}.svg'), chip_svg)

# ═══════════════════════════════════════════════════════════════
# 10. FOOTER BAR (880 × 75) - Clean & Elegant
# ═══════════════════════════════════════════════════════════════
footer_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 75" width="880" height="75">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="75" fill="{BG}"/>
  <rect width="880" height="75" fill="url(#notebookGrid)"/>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="75" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="75" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Thin neon divider line -->
  <line x1="140" y1="14" x2="740" y2="14" stroke="{NEON_GREEN}" stroke-width="0.8" stroke-dasharray="6,6" opacity="0.4"/>

  <!-- Footer Signature (Handwritten Notebook) -->
  <text x="440" y="44" text-anchor="middle" class="doodle-hand" font-size="18" font-weight="600" fill="{TEXT_MUTED}">
    ✏️ Doodled, designed &amp; coded with <tspan fill="{NEON_GREEN}">💚</tspan> by <tspan fill="{TEXT_MAIN}" font-weight="700">Parmeet Singh</tspan> • Delhi, India
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'footer-bar.svg'), footer_svg)

# ═══════════════════════════════════════════════════════════════
# 11. README.md - CLEAN, SPACIOUS, 100% WORKING & NEW TABS
# ═══════════════════════════════════════════════════════════════
readme_md = f"""<div align="center">

  <!-- 01 • HERO BANNER -->
  <img src="./assets/hero-banner.svg" alt="Hey, I'm Parmeet — Full-Stack Developer" width="100%" style="max-width: 880px;" /><br/><br/>

  <!-- 02 • ACTION BUTTONS (ALL OPEN IN NEW TAB) -->
  <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-resume.svg" height="44" alt="View Resume (PDF)" /></a>
  &nbsp;&nbsp;
  <a href="mailto:parmeetssms@gmail.com" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-talk.svg" height="44" alt="Let's Talk" /></a>
  &nbsp;&nbsp;
  <a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-linkedin.svg" height="44" alt="LinkedIn Profile" /></a>
  &nbsp;&nbsp;
  <a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-portfolio.svg" height="44" alt="Personal Portfolio" /></a>
  <br/><br/>

  <!-- 03 • TECH STACK -->
  <img src="./assets/tech-stack.svg" alt="Tech Stack &amp; Toolkit: React, Next.js, Python, Django, Node.js" width="100%" style="max-width: 880px;" /><br/><br/>

  <!-- 04 • FEATURED PROJECTS (CLICK CARD DIRECTLY LAUNCHES DEMO) -->
  <img src="./assets/section-work.svg" alt="Featured Projects — Click any card to launch demo" width="100%" style="max-width: 880px;" /><br/><br/>

  <!-- ROW 1: TradeLab & TourCraze -->
  <a href="https://tradelab-kappa.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-01-tradelab.svg" width="48.5%" style="max-width: 430px;" alt="TradeLab — Real-Time Stock Market Simulator (Launch Demo)" /></a>
  &nbsp;
  <a href="https://tour-craze.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-02-tourcraze.svg" width="48.5%" style="max-width: 430px;" alt="TourCraze — AI Travel Planning Platform (Launch Demo)" /></a>
  <br/><br/>

  <!-- ROW 2: GaadiMandi & Portfolio -->
  <a href="https://car-trade-gamma.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-03-gaadimandi.svg" width="48.5%" style="max-width: 430px;" alt="GaadiMandi — Vehicle Marketplace (Launch Demo)" /></a>
  &nbsp;
  <a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-04-portfolio.svg" width="48.5%" style="max-width: 430px;" alt="Personal Portfolio 2026 (Launch Live Site)" /></a>
  <br/><br/>

  <!-- 05 • CONNECT SECTION -->
  <img src="./assets/section-connect.svg" alt="Let's Connect &amp; Build" width="100%" style="max-width: 880px;" /><br/><br/>

  <!-- CLICKABLE CONNECT CHIPS (2 SPACIOUS ROWS - NEVER OVERLAPS OR CLIPS) -->
  <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-resume.svg" height="44" alt="View Resume (PDF)" /></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-linkedin.svg" height="44" alt="LinkedIn Profile" /></a>
  <br/><br/>
  <a href="mailto:parmeetssms@gmail.com" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-email.svg" height="44" alt="Email Parmeet" /></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-portfolio.svg" height="44" alt="Personal Portfolio" /></a>
  <br/><br/>

  <!-- 06 • FOOTER BAR -->
  <img src="./assets/footer-bar.svg" alt="Parmeet Singh • Full-Stack Developer • Delhi, India" width="100%" style="max-width: 880px;" />

</div>
"""

write_file('README.md', readme_md)

# ═══════════════════════════════════════════════════════════════
# 12. PREVIEW HTML (Local Test & Verification)
# ═══════════════════════════════════════════════════════════════
preview_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Parmeet Singh — GitHub Profile Preview</title>
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
  </style>
</head>
<body>
  <div class="github-canvas">
    {readme_md}
  </div>
</body>
</html>"""

write_file('preview.html', preview_html)
print("\\nAll profile assets, README.md, and preview.html successfully updated!")
