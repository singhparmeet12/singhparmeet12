#!/usr/bin/env python3
"""
generate_neon_doodle_profile.py
Builds Parmeet Singh's Cyber-Doodle Notebook GitHub Profile:
- Clean, Uncluttered Avatar (removed extra emojis around photo and above status badge)
- Removed rocket emojis from Featured Projects header
- Clean Project Cue Cards (removed overlapping emojis, descriptions split into 2 perfectly fitting lines)
- "Let's Talk" button directs to https://personal-portfolio-parmeet1.vercel.app/contact/
- Removed Gmail chip from bottom connect section (now 3 centered, perfectly spaced chips)
- All links configured with target="_blank" rel="noopener noreferrer"
- Spacious, neat layout throughout
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
# 3. HERO BANNER (880 × 420) - Clean, Uncluttered, Elegant
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

  <!-- Main Greeting Group (Clean, Left-aligned, No clutter above status) -->
  <g transform="translate(70, 75)">
    <!-- Clean Status Pill -->
    <rect x="0" y="0" width="144" height="26" rx="13" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1" opacity="0.9"/>
    <circle cx="14" cy="13" r="3.5" fill="{NEON_GREEN}" class="pulse-glow"/>
    <text x="26" y="17" class="mono" font-size="11" font-weight="600" fill="{NEON_GREEN}" letter-spacing="0.5">ONLINE • BUILDING</text>

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

    <!-- Notebook Handwritten Notes & Bio (Generous whitespace, fits perfectly) -->
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

  <!-- Right Floating Sikh Tech Avatar (Clean, no extra emojis around photo) -->
  <g transform="translate(565, 30)">
    <!-- Ambient Neon Backdrop Glow -->
    <ellipse cx="145" cy="180" rx="145" ry="165" fill="url(#avatarBackdropGlow)"/>

    <!-- Subtle Sketched Orbit Ring -->
    <ellipse cx="145" cy="180" rx="135" ry="155" fill="none" stroke="{NEON_GREEN}" stroke-width="1.2" stroke-dasharray="6,8" opacity="0.3" class="connecting-line"/>

    <!-- Floating Avatar with Laptop -->
    <g class="floating-avatar">
      <image href="data:image/png;base64,{AVATAR_B64}" x="20" y="10" width="250" height="340" preserveAspectRatio="xMidYMid meet"/>
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
# 5. TECH STACK & TOOLKIT (880 × 265) - Clean & Focused
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
# 6. SELECTED WORK HEADER (880 × 95) - NO ROCKET EMOJIS
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

  <!-- Header Badge (NO ROCKET EMOJIS) -->
  <g transform="translate(285, 20)">
    <rect x="0" y="0" width="310" height="38" rx="19" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="155" y="25" text-anchor="middle" class="doodle-hand" font-size="22" font-weight="700" fill="{NEON_CYAN}" letter-spacing="1">
      ✦ FEATURED PROJECTS ✦
    </text>
  </g>

  <!-- Handwritten Sub-note -->
  <text x="440" y="80" text-anchor="middle" class="doodle-hand" font-size="17" fill="{TEXT_MUTED}">
    ↙ click any card to launch the live interactive app ↘
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'section-work.svg'), section_work_svg)

# ═══════════════════════════════════════════════════════════════
# 7. PROJECT CARDS (430 × 205) - Zero Overlapping Doodles, 2 Safe Lines
# ═══════════════════════════════════════════════════════════════
projects = [
    {
        'num': '01',
        'file': 'card-01-tradelab',
        'title': 'TradeLab',
        'type': 'STOCK MARKET SIMULATOR',
        'desc1': 'Real-time stock market simulator with',
        'desc2': 'virtual trading &amp; live portfolio tracking.',
        'tech': 'React • Node.js • MongoDB • Chart.js',
        'badge': '● LIVE SIMULATOR',
        'accent': NEON_GREEN,
    },
    {
        'num': '02',
        'file': 'card-02-tourcraze',
        'title': 'TourCraze',
        'type': 'SMART TRAVEL BOOKING',
        'desc1': 'AI-powered smart travel planning platform',
        'desc2': 'with curated tours &amp; instant booking.',
        'tech': 'React • Express • MongoDB • Tailwind',
        'badge': '● LIVE PLATFORM',
        'accent': NEON_CYAN,
    },
    {
        'num': '03',
        'file': 'card-03-gaadimandi',
        'title': 'GaadiMandi',
        'type': 'VEHICLE MARKETPLACE',
        'desc1': 'Full-stack automotive trading marketplace',
        'desc2': 'with verified listings &amp; dealer analytics.',
        'tech': 'Python • Django • PostgreSQL • Tailwind',
        'badge': '● LIVE MARKETPLACE',
        'accent': NEON_GOLD,
    },
    {
        'num': '04',
        'file': 'card-04-portfolio',
        'title': 'Personal Portfolio',
        'type': 'DEVELOPER SHOWCASE',
        'desc1': 'Interactive 3D developer showcase with',
        'desc2': 'motion animations &amp; responsive design.',
        'tech': 'Next.js • TailwindCSS • Framer Motion',
        'badge': '● LIVE SITE',
        'accent': NEON_GREEN,
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
  <rect x="3" y="28" width="4" height="145" rx="2" fill="{acc}"/>

  <!-- Top Notebook Tape Header Accent -->
  <polygon points="25,3 110,3 105,14 20,14" fill="{acc}" opacity="0.25"/>

  <!-- Status Beacon Badge (Right aligned) -->
  <g transform="translate(290, 18)">
    <rect x="0" y="0" width="122" height="22" rx="11" fill="{BG}" stroke="{acc}" stroke-width="1"/>
    <circle cx="14" cy="11" r="3.5" fill="{acc}"/>
    <circle cx="14" cy="11" r="3.5" fill="none" stroke="{acc}" stroke-width="1.5" class="radar-pulse"/>
    <text x="24" y="15" class="mono" font-size="9" font-weight="700" fill="{acc}" letter-spacing="0.5">{p['badge']}</text>
  </g>

  <!-- Project Number & Category -->
  <text x="22" y="44" class="mono" font-size="12" font-weight="700" fill="{acc}" letter-spacing="1">{p['num']} // {p['type']}</text>

  <!-- Project Title (Size 26: never collides with badge) -->
  <text x="22" y="74" class="doodle-hand" font-size="26" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.5">{p['title']}</text>

  <!-- 2 Clean Short Lines: Never Out of Box, Zero Overlap -->
  <text x="22" y="103" class="doodle-hand" font-size="16" fill="{TEXT_MUTED}">{p['desc1']}</text>
  <text x="22" y="125" class="doodle-hand" font-size="16" fill="{TEXT_MUTED}">{p['desc2']}</text>

  <!-- Tech Stack Pills -->
  <g transform="translate(22, 143)">
    <text x="0" y="11" class="mono" font-size="11.5" font-weight="600" fill="{NEON_CYAN}" opacity="0.88">{p['tech']}</text>
  </g>

  <!-- Launch Prompt Bar (Click Card To Launch) -->
  <g transform="translate(22, 166)">
    <rect x="0" y="0" width="386" height="25" rx="7" fill="{BG}" stroke="{acc}" stroke-width="1" opacity="0.9"/>
    <text x="193" y="17" text-anchor="middle" class="mono" font-size="10.5" font-weight="700" fill="{acc}" letter-spacing="1">
      CLICK CARD TO LAUNCH LIVE APP ↗
    </text>
  </g>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f"{p['file']}.svg"), card_svg)

# ═══════════════════════════════════════════════════════════════
# 8. CONNECT SECTION (880 × 110) - Clean & Elegant
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
  <line x1="440" y1="0" x2="440" y2="22" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>

  <!-- Header Badge -->
  <g transform="translate(285, 22)">
    <rect x="0" y="0" width="310" height="40" rx="20" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="155" y="26" text-anchor="middle" class="doodle-hand" font-size="22" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1">
      💬 LET'S CONNECT &amp; BUILD 💬
    </text>
  </g>

  <!-- Friendly Handwritten Note (Generous spacing) -->
  <text x="440" y="88" text-anchor="middle" class="doodle-hand" font-size="18" fill="{TEXT_MUTED}">
    Always excited for new projects, full-time opportunities, or tech discussions!
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'section-connect.svg'), section_connect_svg)

# ═══════════════════════════════════════════════════════════════
# 9. CONNECT CHIPS (3 Clickable Badges - Resume, LinkedIn, Portfolio)
# ═══════════════════════════════════════════════════════════════
chips = [
    ('resume',    '📄 View Resume (PDF)', 195, NEON_GREEN),
    ('linkedin',  '💼 LinkedIn Profile',  185, NEON_CYAN),
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
# 11. README.md - CLEAN, SPACIOUS, 100% WORKING LINKS
# ═══════════════════════════════════════════════════════════════
readme_md = f"""<div align="center">

  <!-- 01 • HERO BANNER -->
  <img src="./assets/hero-banner.svg" alt="Hey, I'm Parmeet — Full-Stack Developer" width="100%" style="max-width: 880px;" /><br/><br/>

  <!-- 02 • ACTION BUTTONS (ALL WITH TARGET=_BLANK FOR NEW TAB) -->
  <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-resume.svg" height="44" alt="View Resume (PDF)" /></a>
  &nbsp;&nbsp;
  <a href="https://personal-portfolio-parmeet1.vercel.app/contact/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-talk.svg" height="44" alt="Let's Talk" /></a>
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

  <!-- CLICKABLE CONNECT CHIPS (3 CLEAN, SPACIOUS CHIPS - CENTERED) -->
  <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-resume.svg" height="44" alt="View Resume (PDF)" /></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-linkedin.svg" height="44" alt="LinkedIn Profile" /></a>
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
