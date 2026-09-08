#!/usr/bin/env python3
"""
generate_neon_doodle_profile.py
Builds Parmeet Singh's Cyber-Doodle Notebook GitHub Profile:
- 100% Seamless in BOTH Light Mode and Dark Mode (ZERO white horizontal lines anywhere!)
  - Uses align="top" on every <img> tag to eliminate browser font descender strut gap (0.00px gap)
  - Full-width tiled button bar (4 x 220px = 880px solid dark background, 25% each)
  - Full-width tiled project cards (2 x 440px = 880px solid dark background, 50% each)
  - Full-width tiled connect chips (3 chips: 293+294+293 = 880px solid dark background)
  - Zero <br/> tags and zero &nbsp;
  - HTML comments (<!-- -->) between images eliminate all inline whitespace
- Avatar Floating Upgrade:
  - Fast, buoyant float ("above and low"): 20px vertical travel (+4px to -16px) at 2.8s period
- Lightweight Criss-Cross Doodle Satellites:
  - Lighter, airy, delicate vector doodle capsules (r=15.5px, soft semi-transparent fill, crisp glow)
  - Criss-cross orbital paths: Orbit 1 tilted at -24°, Orbit 2 tilted at +24°, Orbit 3 undulating loop
  - Smooth, serene, un-chaotic periods (19s, 24s, 21s)
  - Upright counter-rotation ensures doodles remain upright
  - 138px safe clearance from bio text, 25px clearance from avatar
- Living Constellation of Animated Stars:
  - Highly visible twinkling stars flowing from top-left corner right up to and around Parmeet's name!
  - Vibrant 4-point stars with neon glows and white cores above and next to "Parmeet"
- Project Cue Cards Polish:
  - Accurate stack: Python & Django based (no React), max 4 skills each!
  - Fixed Neon Icon Spacing: Fixed X positions (x=265 left card, x=210 right card) leaving 34px-85px of clean space — ZERO overlap!
  - No launch button bar (heading already conveys it)
- Tech Stack Polish:
  - Fixed Backend Card text overflow (all lines fit comfortably within box)
- Connect Section Header Polish:
  - Widened badge to 350px with generous 30px padding so "L" never overlaps the rounded pill arc!
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
      <feFlood flood-color="{NEON_GREEN}" flood-opacity="0.65" result="color"/>
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
      <feFlood flood-color="{NEON_CYAN}" flood-opacity="0.6" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="softGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feFlood flood-color="{NEON_GREEN}" flood-opacity="0.45" result="color"/>
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
    /* Lively buoyancy: 20px vertical travel (+4px to -16px) at 2.8s period */
    @keyframes floatAvatar {{
      0%, 100% {{ transform: translateY(4px) rotate(0deg); }}
      50% {{ transform: translateY(-16px) rotate(-1.5deg); }}
    }}
    @keyframes orbitCrissA {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(-360deg); }}
    }}
    @keyframes orbitCrissB {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    @keyframes orbitCounterA {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    @keyframes orbitCounterB {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(-360deg); }}
    }}
    /* Highly visible twinkling stars around Parmeet's name */
    @keyframes twinkleStar {{
      0%, 100% {{ opacity: 0.45; transform: scale(0.85); }}
      50% {{ opacity: 1; transform: scale(1.35); }}
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
    @keyframes dashTravel {{
      to {{ stroke-dashoffset: -32; }}
    }}
    .floating-avatar {{ animation: floatAvatar 2.8s ease-in-out infinite; transform-origin: center; }}
    .orbit-a {{ animation: orbitCrissA 19s linear infinite; transform-origin: 0px 0px; }}
    .orbit-b {{ animation: orbitCrissB 24s linear infinite; transform-origin: 0px 0px; }}
    .counter-a {{ animation: orbitCounterA 19s linear infinite; transform-origin: 0px 0px; }}
    .counter-b {{ animation: orbitCounterB 24s linear infinite; transform-origin: 0px 0px; }}
    .star-twinkle-1 {{ animation: twinkleStar 2.2s ease-in-out infinite; transform-origin: center; }}
    .star-twinkle-2 {{ animation: twinkleStar 2.8s ease-in-out infinite 0.7s; transform-origin: center; }}
    .star-twinkle-3 {{ animation: twinkleStar 3.2s ease-in-out infinite 1.4s; transform-origin: center; }}
    .cursor-blink {{ animation: blinkCursor 0.9s infinite; }}
    .pulse-glow {{ animation: pulseNeon 2.8s ease-in-out infinite; }}
    .radar-pulse {{ animation: radarPing 2s cubic-bezier(0, 0.2, 0.8, 1) infinite; }}
    .connecting-line {{ stroke-dasharray: 6, 6; animation: dashTravel 2s linear infinite; }}
  ]]></style>
"""

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"[OK] Generated {filename}")

# ═══════════════════════════════════════════════════════════════
# 3. HERO BANNER (880 × 410) - Lively Avatar, Visible Stars & Light Doodles
# ═══════════════════════════════════════════════════════════════
hero_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 880 410" width="880" height="410">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Seamless Canvas Background -->
  <rect width="880" height="410" fill="{BG}"/>
  <rect width="880" height="410" fill="url(#notebookGrid)"/>

  <!-- Top Notebook Washi Tape Accent -->
  <polygon points="40,14 180,12 178,30 38,32" fill="{NEON_GREEN}" opacity="0.18"/>
  <text x="109" y="25" text-anchor="middle" class="mono" font-size="10" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1.5">PARMEET.DEV // 2026</text>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="410" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="410" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- ═══ VIBRANT CONSTELLATION: Stars Twinkling from Top-Left up to Parmeet's Name ═══ -->
  <!-- 1. Top-Left Corner Star (near margin lines) -->
  <g class="star-twinkle-1" transform="translate(68, 42)">
    <path d="M 0,-8 L 2,-2 L 8,0 L 2,2 L 0,8 L -2,2 L -8,0 L -2,-2 Z" fill="{NEON_CYAN}" filter="url(#softGlow)"/>
    <circle cx="0" cy="0" r="1.5" fill="#FFFFFF"/>
  </g>

  <!-- 2. Cute Cross Sparkle above Status Pill -->
  <g class="star-twinkle-2" transform="translate(155, 48)">
    <path d="M -6,0 L 6,0 M 0,-6 L 0,6" stroke="{NEON_GREEN}" stroke-width="1.6" stroke-linecap="round" filter="url(#softGlow)"/>
    <circle cx="0" cy="0" r="1.2" fill="{NEON_GREEN}"/>
  </g>

  <!-- 3. Golden Star between Status Pill and Hey -->
  <g class="star-twinkle-3" transform="translate(235, 92)">
    <circle cx="0" cy="0" r="2.5" fill="{NEON_GOLD}" filter="url(#softGlow)"/>
    <path d="M -6,0 L 6,0 M 0,-6 L 0,6" stroke="{NEON_GOLD}" stroke-width="1.2" stroke-linecap="round"/>
  </g>

  <!-- 4. Bright Neon Green 4-Point Star directly above 'Parmeet' -->
  <g class="star-twinkle-1" transform="translate(325, 115)">
    <path d="M 0,-11 L 2.8,-2.8 L 11,0 L 2.8,2.8 L 0,11 L -2.8,2.8 L -11,0 L -2.8,-2.8 Z" fill="{NEON_GREEN}" filter="url(#neonGlowGreen)"/>
    <circle cx="0" cy="0" r="2.2" fill="#FFFFFF"/>
  </g>

  <!-- 5. Electric Cyan Star right next to 'Parmeet!' Exclamation Mark -->
  <g class="star-twinkle-2" transform="translate(398, 142)">
    <path d="M 0,-9 L 2.4,-2.4 L 9,0 L 2.4,2.4 L 0,9 L -2.4,2.4 L -9,0 L -2.4,-2.4 Z" fill="{NEON_CYAN}" filter="url(#neonGlowCyan)"/>
    <circle cx="0" cy="0" r="1.8" fill="#FFFFFF"/>
  </g>

  <!-- 6. Cute Neon Pink Sparkle under the Underline -->
  <g class="star-twinkle-3" transform="translate(355, 182)">
    <path d="M -4,0 L 4,0 M 0,-4 L 0,4" stroke="{NEON_PINK}" stroke-width="1.4" stroke-linecap="round" filter="url(#softGlow)"/>
  </g>

  <!-- 7. Ambient Twinkle near Bio text -->
  <g class="star-twinkle-1" transform="translate(505, 110)">
    <circle cx="0" cy="0" r="2" fill="{NEON_CYAN}" opacity="0.85"/>
    <path d="M -4,0 L 4,0 M 0,-4 L 0,4" stroke="{NEON_CYAN}" stroke-width="0.8" opacity="0.8"/>
  </g>

  <!-- Main Greeting Group (Clean, Left-aligned) -->
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
        const stack = ["Python", "Django", "PostgreSQL", "Tailwind"];<tspan fill="{NEON_GREEN}" class="cursor-blink">▋</tspan>
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

  <!-- Right Floating Sikh Tech Avatar + 3 Lightweight Criss-Cross Doodle Satellites -->
  <g transform="translate(565, 30)">
    <!-- Ambient Neon Backdrop Glow -->
    <ellipse cx="145" cy="175" rx="145" ry="160" fill="url(#avatarBackdropGlow)"/>

    <!-- Subtle Criss-Cross Dashed Orbital Guide Tracks -->
    <ellipse cx="145" cy="175" rx="148" ry="102" transform="rotate(-24, 145, 175)" fill="none" stroke="{NEON_GREEN}" stroke-width="0.9" stroke-dasharray="4,8" opacity="0.2"/>
    <ellipse cx="145" cy="175" rx="148" ry="102" transform="rotate(24, 145, 175)" fill="none" stroke="{NEON_CYAN}" stroke-width="0.9" stroke-dasharray="4,8" opacity="0.2"/>

    <!-- Floating Avatar with Laptop (Noticeable 20px buoyant vertical float at 2.8s) -->
    <g class="floating-avatar">
      <image href="data:image/png;base64,{AVATAR_B64}" x="20" y="5" width="250" height="340" preserveAspectRatio="xMidYMid meet"/>
    </g>

    <!-- ═══ 3 LIGHTWEIGHT CRISS-CROSS DOODLE SATELLITES ═══ -->
    <!-- Lightweight, airy, luminous (r=15.5px, semi-transparent fill, delicate glow) -->

    <!-- ORBIT 1: Tilted -24° (Doodle Laptop 💻) -->
    <g transform="translate(145, 175) rotate(-24)">
      <g class="orbit-a">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="19s" repeatCount="indefinite"/>
        <!-- Position on ellipse (146, 0) -->
        <g transform="translate(146, 0)">
          <g class="counter-a">
            <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="19s" repeatCount="indefinite"/>
            <!-- Upright Counter-Tilt (+24°) -->
            <g transform="rotate(24)">
              <circle cx="0" cy="0" r="16.5" fill="{NEON_CYAN}" opacity="0.15" filter="url(#softGlow)"/>
              <circle cx="0" cy="0" r="15.5" fill="{BG_SURFACE}" fill-opacity="0.8" stroke="{NEON_CYAN}" stroke-width="1.3"/>
              <!-- Lightweight Hand-Drawn Doodle Laptop Icon -->
              <g transform="translate(0, -1)">
                <rect x="-8.5" y="-6" width="17" height="11" rx="1.5" fill="{BG}" stroke="{NEON_CYAN}" stroke-width="1.2"/>
                <text x="-3.5" y="1.5" font-family="'JetBrains Mono', monospace" font-size="6" font-weight="700" fill="{NEON_GREEN}">&gt;_</text>
                <line x1="-11" y1="5" x2="11" y2="5" stroke="{NEON_CYAN}" stroke-width="1.6" stroke-linecap="round"/>
              </g>
            </g>
          </g>
        </g>
      </g>
    </g>

    <!-- ORBIT 2: Tilted +24° (Doodle Coffee Mug ☕) -->
    <g transform="translate(145, 175) rotate(24)">
      <g class="orbit-b">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="24s" repeatCount="indefinite"/>
        <!-- Position on ellipse (-146, 0) -->
        <g transform="translate(-146, 0)">
          <g class="counter-b">
            <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="24s" repeatCount="indefinite"/>
            <!-- Upright Counter-Tilt (-24°) -->
            <g transform="rotate(-24)">
              <circle cx="0" cy="0" r="16.5" fill="{NEON_GOLD}" opacity="0.15" filter="url(#softGlow)"/>
              <circle cx="0" cy="0" r="15.5" fill="{BG_SURFACE}" fill-opacity="0.8" stroke="{NEON_GOLD}" stroke-width="1.3"/>
              <!-- Lightweight Hand-Drawn Doodle Coffee Mug Icon -->
              <g transform="translate(-1, 1.5)">
                <rect x="-6" y="-5" width="12" height="11" rx="2.5" fill="{BG}" stroke="{NEON_GOLD}" stroke-width="1.2"/>
                <path d="M 6,-2.5 C 9.5,-2.5 9.5,2.5 6,2.5" fill="none" stroke="{NEON_GOLD}" stroke-width="1.2" stroke-linecap="round"/>
                <!-- Delicate Steam Squiggles -->
                <path d="M -2.5,-8.5 Q -1,-6.5 -2.5,-5" fill="none" stroke="{NEON_GREEN}" stroke-width="0.9" stroke-linecap="round"/>
                <path d="M 1.5,-8.5 Q 3,-6.5 1.5,-5" fill="none" stroke="{NEON_GREEN}" stroke-width="0.9" stroke-linecap="round"/>
              </g>
            </g>
          </g>
        </g>
      </g>
    </g>

    <!-- SATELLITE 3: Lightweight Twinkle Doodle Star ✨ (Undulating 21s Orbit) -->
    <g transform="translate(145, 175)">
      <g class="orbit-a">
        <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-360 0 0" dur="21s" repeatCount="indefinite"/>
        <!-- Position at top (0, -148) -->
        <g transform="translate(0, -148)">
          <g class="counter-a">
            <animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="21s" repeatCount="indefinite"/>
            <circle cx="0" cy="0" r="16" fill="{NEON_GREEN}" opacity="0.15" filter="url(#softGlow)"/>
            <circle cx="0" cy="0" r="15" fill="{BG_SURFACE}" fill-opacity="0.8" stroke="{NEON_GREEN}" stroke-width="1.3"/>
            <!-- Delicate 4-Point Star -->
            <path d="M 0,-8 L 2,-2 L 8,0 L 2,2 L 0,8 L -2,2 L -8,0 L -2,-2 Z" fill="{NEON_GREEN}"/>
            <circle cx="0" cy="0" r="1.6" fill="#FFFFFF"/>
          </g>
        </g>
      </g>
    </g>
  </g>

  <!-- Bottom Connecting Neon Guide (Flows into buttons) -->
  <line x1="440" y1="375" x2="440" y2="410" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="408" r="3" fill="{NEON_GREEN}"/>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'hero-banner.svg'), hero_svg)

# ═══════════════════════════════════════════════════════════════
# 4. ACTION BUTTONS (4 × 220px = 880px Solid Dark Tiled Bar)
# ═══════════════════════════════════════════════════════════════
# Pill positions customized so View Resume is safely INSIDE the left margin line (x=45, 49)
buttons_data = [
    # id, label, color, has_left_margin, has_center_line, pill_x, pill_w, text_x, font_size
    ('resume',    '📄 View Resume', NEON_GREEN, True,  False, 58, 154, 135, 17),
    ('talk',      '💬 Let\'s Talk',  NEON_CYAN,  False, True,  24, 168, 108, 17.5),
    ('linkedin',  '💼 LinkedIn',    NEON_GOLD,  False, False, 28, 168, 112, 17.5),
    ('portfolio', '🌐 Portfolio',   NEON_GREEN, False, False, 8,  154, 85,  17),
]

for b_id, label, color, has_left_margin, has_center_line, px, pw, tx, fs in buttons_data:
    left_line = f"""
      <line x1="45" y1="0" x2="45" y2="54" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
      <line x1="49" y1="0" x2="49" y2="54" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>
    """ if has_left_margin else ""

    center_line = f"""
      <line x1="220" y1="0" x2="220" y2="54" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
    """ if has_center_line else ""

    btn_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 54" width="220" height="54">
  <defs>
    {COMMON_DEFS}
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

  <!-- Full-bleed dark background tiles seamlessly into 880px container -->
  <rect width="220" height="54" fill="{BG}"/>
  <rect width="220" height="54" fill="url(#notebookGrid)"/>
  {left_line}
  {center_line}

  <!-- Button Pill: Safely placed, zero collision with margin lines -->
  <rect x="{px}" y="6" width="{pw}" height="42" rx="21" fill="{BG_SURFACE}"/>
  <rect x="{px}" y="6" width="{pw}" height="42" rx="21" fill="none" stroke="{color}" stroke-width="1.6" class="btn-border" filter="url(#btnGlow_{b_id})"/>

  <!-- Button Label -->
  <text x="{tx}" y="32" text-anchor="middle" class="doodle-hand" font-size="{fs}" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.3">
    {label}
  </text>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f'btn-{b_id}.svg'), btn_svg)

# ═══════════════════════════════════════════════════════════════
# 5. TECH STACK & TOOLKIT (880 × 265) - Guaranteed Zero Overflow!
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

  <!-- 3 Categorized Skill Cards (Widened to 240px, safe font-size 15, concise lines for generous >45px margin!) -->
  <!-- Card 1: Frontend -->
  <g transform="translate(60, 118)">
    <rect x="0" y="0" width="240" height="118" rx="12" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.2"/>
    <rect x="12" y="10" width="100" height="20" rx="6" fill="{BG}"/>
    <text x="18" y="24" class="mono" font-size="10.5" font-weight="700" fill="{NEON_GREEN}">01 // FRONTEND</text>
    <text x="14" y="52" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• HTML5 &amp; CSS3</text>
    <text x="14" y="74" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• JavaScript &amp; Modern UI</text>
    <text x="14" y="96" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• Tailwind &amp; Bootstrap</text>
  </g>

  <!-- Card 2: Backend -->
  <g transform="translate(320, 118)">
    <rect x="0" y="0" width="240" height="118" rx="12" fill="{BG_SURFACE}" stroke="{NEON_CYAN}" stroke-width="1.2"/>
    <rect x="12" y="10" width="104" height="20" rx="6" fill="{BG}"/>
    <text x="18" y="24" class="mono" font-size="10.5" font-weight="700" fill="{NEON_CYAN}">02 // BACKEND</text>
    <text x="14" y="52" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• Python &amp; Django</text>
    <text x="14" y="74" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• Django REST (DRF)</text>
    <text x="14" y="96" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• WebSockets &amp; APIs</text>
  </g>

  <!-- Card 3: Databases & DevOps -->
  <g transform="translate(580, 118)">
    <rect x="0" y="0" width="240" height="118" rx="12" fill="{BG_SURFACE}" stroke="{NEON_GOLD}" stroke-width="1.2"/>
    <rect x="12" y="10" width="124" height="20" rx="6" fill="{BG}"/>
    <text x="18" y="24" class="mono" font-size="10.5" font-weight="700" fill="{NEON_GOLD}">03 // DATA &amp; CLOUD</text>
    <text x="14" y="52" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• PostgreSQL &amp; SQLite</text>
    <text x="14" y="74" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• Redis &amp; Caching</text>
    <text x="14" y="96" class="doodle-hand" font-size="15" fill="{TEXT_MAIN}">• Git, Docker &amp; Cloud</text>
  </g>

  <!-- Continuous Flow Line to Projects -->
  <line x1="440" y1="236" x2="440" y2="265" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="263" r="3" fill="{NEON_GREEN}"/>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'tech-stack.svg'), tech_stack_svg)

# ═══════════════════════════════════════════════════════════════
# 6. SELECTED WORK HEADER (880 × 95) - Clean, No Rocket Emoji
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

  <!-- Header Badge (Clean) -->
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
# 7. PROJECT CARDS (440 × 170) - 100% NEON Vector Icons (Zero Overlap!)
# ═══════════════════════════════════════════════════════════════
# Accurate Real Stack: Python & Django based (no React), max 4 skills each!
# Fixed safe icon X positions:
# - Left cards: icon at x=265 (ends at x=297). Title ends before x=231 -> 34px-70px clean gap!
# - Right cards: icon at x=210 (ends at x=242). Title ends before x=173 -> 37px-85px clean gap!
# ZERO overlap guaranteed!
projects = [
    {
        'num': '01',
        'file': 'card-01-tradelab',
        'title': 'TradeLab',
        'type': 'STOCK MARKET SIMULATOR',
        'desc1': 'Real-time stock market simulator with',
        'desc2': 'virtual trading &amp; live portfolio tracking.',
        'tech': 'Python • Django • Chart.js • Bootstrap',
        'badge': '● LIVE SIMULATOR',
        'accent': NEON_GREEN,
        'is_left': True,
        'neon_icon': f"""
          <!-- Glowing Neon Green Stock Market Trend Doodle -->
          <path d="M 0,13 L 6,8 L 12,11 L 18,3 L 24,5 L 30,-2" fill="none" stroke="{NEON_GREEN}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" filter="url(#softGlow)"/>
          <polygon points="26,-3 32,-3 32,3" fill="{NEON_GREEN}"/>
          <line x1="6" y1="5" x2="6" y2="12" stroke="{NEON_GREEN}" stroke-width="1.1" opacity="0.75"/>
          <rect x="4.5" y="7" width="3" height="3.5" fill="{NEON_GREEN}" rx="0.5"/>
          <line x1="18" y1="1" x2="18" y2="8" stroke="{NEON_GREEN}" stroke-width="1.1" opacity="0.75"/>
          <rect x="16.5" y="3" width="3" height="4" fill="{NEON_GREEN}" rx="0.5"/>
        """,
    },
    {
        'num': '02',
        'file': 'card-02-tourcraze',
        'title': 'TourCraze',
        'type': 'SMART TRAVEL BOOKING',
        'desc1': 'Smart AI travel planning platform with',
        'desc2': 'curated tour discovery &amp; instant booking.',
        'tech': 'Python • Django • PostgreSQL • Tailwind',
        'badge': '● LIVE PLATFORM',
        'accent': NEON_CYAN,
        'is_left': False,
        'neon_icon': f"""
          <!-- Glowing Neon Electric Cyan Supersonic Jet Doodle -->
          <path d="M -6,13 Q 3,11 10,6" fill="none" stroke="{NEON_CYAN}" stroke-width="1.2" stroke-dasharray="2,2" opacity="0.75"/>
          <polygon points="12,-3 30,2 16,13 15,6" fill="{BG}" stroke="{NEON_CYAN}" stroke-width="1.8" stroke-linejoin="round" filter="url(#softGlow)"/>
          <polygon points="12,-3 30,2 16,13 15,6" fill="{NEON_CYAN}" opacity="0.3"/>
          <line x1="12" y1="-3" x2="16" y2="13" stroke="{NEON_CYAN}" stroke-width="1.2"/>
        """,
    },
    {
        'num': '03',
        'file': 'card-03-gaadimandi',
        'title': 'GaadiMandi',
        'type': 'VEHICLE MARKETPLACE',
        'desc1': 'Full-stack automotive marketplace with',
        'desc2': 'verified listings &amp; dealer analytics.',
        'tech': 'Python • Django • PostgreSQL • Tailwind',
        'badge': '● LIVE MARKETPLACE',
        'accent': NEON_GOLD,
        'is_left': True,
        'neon_icon': f"""
          <!-- Glowing Neon Gold Sports Car Profile Doodle -->
          <path d="M 0,11 L 4,5 L 11,2 L 22,2 L 28,6 L 35,8 L 35,12 L 0,12 Z" fill="{BG}" stroke="{NEON_GOLD}" stroke-width="1.8" stroke-linejoin="round" filter="url(#softGlow)"/>
          <path d="M 0,11 L 4,5 L 11,2 L 22,2 L 28,6 L 35,8 L 35,12 L 0,12 Z" fill="{NEON_GOLD}" opacity="0.25"/>
          <circle cx="8" cy="12" r="3" fill="{BG}" stroke="{NEON_GOLD}" stroke-width="1.6"/>
          <circle cx="27" cy="12" r="3" fill="{BG}" stroke="{NEON_GOLD}" stroke-width="1.6"/>
          <line x1="35" y1="9" x2="41" y2="9" stroke="{NEON_GOLD}" stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>
        """,
    },
    {
        'num': '04',
        'file': 'card-04-portfolio',
        'title': 'Portfolio',
        'type': 'DEVELOPER SHOWCASE',
        'desc1': 'Interactive developer showcase with',
        'desc2': 'smooth animations &amp; creative layout.',
        'tech': 'Python • Django • JavaScript • Tailwind',
        'badge': '● LIVE SITE',
        'accent': NEON_GREEN,
        'is_left': False,
        'neon_icon': f"""
          <!-- Glowing Neon Green Lightning Bolt Doodle -->
          <polygon points="12,-4 3,7 10,7 6,17 19,4 11,4" fill="{NEON_GREEN}" stroke="{NEON_GREEN}" stroke-width="1.4" stroke-linejoin="round" filter="url(#softGlow)"/>
          <polygon points="12,-4 3,7 10,7 6,17 19,4 11,4" fill="#FFFFFF" opacity="0.55"/>
        """,
    },
]

for p in projects:
    acc = p['accent']
    is_left = p['is_left']

    if is_left:
        left_margin_code = f"""
          <line x1="45" y1="0" x2="45" y2="170" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
          <line x1="49" y1="0" x2="49" y2="170" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>
        """
        box_x = 58
        content_x = 76
        tape_points = "75,3 160,3 155,14 70,14"
        badge_x = 296
        # Fixed safe X position: 265px (title ends <= 231, leaving 34px-70px padding!)
        icon_x = 265
    else:
        left_margin_code = ""
        box_x = 10
        content_x = 28
        tape_points = "28,3 113,3 108,14 23,14"
        badge_x = 248
        # Fixed safe X position: 210px (title ends <= 173, leaving 37px-85px padding!)
        icon_x = 210

    card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 170" width="440" height="170">
  <defs>
    {COMMON_DEFS}
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

  <!-- Full-bleed outer dark canvas (Tiles seamlessly to 880px) -->
  <rect width="440" height="170" fill="{BG}"/>
  <rect width="440" height="170" fill="url(#notebookGrid)"/>
  {left_margin_code}

  <!-- Card Surface (Doodle Notebook Card, width 372px) -->
  <rect x="{box_x}" y="3" width="372" height="164" rx="16" fill="{BG_SURFACE}"/>

  <!-- Sketched Doodle Neon Border -->
  <rect x="{box_x}" y="3" width="372" height="164" rx="16" fill="none" stroke="{acc}" stroke-width="1.5" class="glow-border" filter="url(#cardGlow_{p['num']})"/>

  <!-- Left Accent Notch -->
  <rect x="{box_x}" y="26" width="4" height="118" rx="2" fill="{acc}"/>

  <!-- Top Notebook Tape Header Accent -->
  <polygon points="{tape_points}" fill="{acc}" opacity="0.25"/>

  <!-- Status Beacon Badge (Right aligned) -->
  <g transform="translate({badge_x}, 16)">
    <rect x="0" y="0" width="122" height="22" rx="11" fill="{BG}" stroke="{acc}" stroke-width="1"/>
    <circle cx="14" cy="11" r="3.5" fill="{acc}"/>
    <circle cx="14" cy="11" r="3.5" fill="none" stroke="{acc}" stroke-width="1.5" class="radar-pulse"/>
    <text x="24" y="15" class="mono" font-size="9" font-weight="700" fill="{acc}" letter-spacing="0.5">{p['badge']}</text>
  </g>

  <!-- Project Number & Category -->
  <text x="{content_x}" y="38" class="mono" font-size="11.5" font-weight="700" fill="{acc}" letter-spacing="1">{p['num']} // {p['type']}</text>

  <!-- Project Title -->
  <text x="{content_x}" y="68" class="doodle-hand" font-size="26" font-weight="700" fill="{TEXT_MAIN}" letter-spacing="0.5">
    {p['title']}
  </text>

  <!-- Custom Glowing NEON Vector Doodle Icon (Generous safe spacing: ZERO text overlap!) -->
  <g transform="translate({icon_x}, 53)">
    {p['neon_icon']}
  </g>

  <!-- 2 Clean Short Lines: Generous Space, Zero Overlap -->
  <text x="{content_x}" y="98" class="doodle-hand" font-size="15.5" fill="{TEXT_MUTED}">{p['desc1']}</text>
  <text x="{content_x}" y="120" class="doodle-hand" font-size="15.5" fill="{TEXT_MUTED}">{p['desc2']}</text>

  <!-- Tech Stack Pills (Real stack: Python & Django based, max 4 skills!) -->
  <g transform="translate({content_x}, 143)">
    <text x="0" y="11" class="mono" font-size="11" font-weight="600" fill="{NEON_CYAN}" opacity="0.88">{p['tech']}</text>
  </g>
</svg>"""
    write_file(os.path.join(ASSETS_DIR, f"{p['file']}.svg"), card_svg)

# ═══════════════════════════════════════════════════════════════
# 8. CONNECT SECTION (880 × 110) - Generous Badge Width (No 'L' Overlap!)
# ═══════════════════════════════════════════════════════════════
# 8. CONNECT SECTION (880 × 130) - Full-Sized Connecting Line & Clean Badge
# ═══════════════════════════════════════════════════════════════
section_connect_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 130" width="880" height="130">
  {COMMON_DEFS}
  {COMMON_STYLES}

  <!-- Background -->
  <rect width="880" height="130" fill="{BG}"/>
  <rect width="880" height="130" fill="url(#notebookGrid)"/>

  <!-- Left Continuous Margin Guide Line -->
  <line x1="45" y1="0" x2="45" y2="130" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
  <line x1="49" y1="0" x2="49" y2="130" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>

  <!-- Continuous Flow Line entering from projects (Full-sized, prominent line + glowing node!) -->
  <line x1="440" y1="0" x2="440" y2="38" stroke="{NEON_GREEN}" stroke-width="2" stroke-dasharray="4,4" class="connecting-line"/>
  <circle cx="440" cy="38" r="4" fill="{NEON_GREEN}" filter="url(#softGlow)"/>

  <!-- Header Badge: 350px width, centered at 265 (Clean text, NO emojis) -->
  <g transform="translate(265, 46)">
    <rect x="0" y="0" width="350" height="42" rx="21" fill="{BG_SURFACE}" stroke="{NEON_GREEN}" stroke-width="1.5" filter="url(#softGlow)"/>
    <text x="175" y="27" text-anchor="middle" class="doodle-hand" font-size="21" font-weight="700" fill="{NEON_GREEN}" letter-spacing="1.5">
      LET'S CONNECT &amp; BUILD
    </text>
  </g>

  <!-- Friendly Handwritten Note (Generous spacing) -->
  <text x="440" y="112" text-anchor="middle" class="doodle-hand" font-size="18" fill="{TEXT_MUTED}">
    Always excited for new projects, full-time opportunities, or tech discussions!
  </text>
</svg>"""

write_file(os.path.join(ASSETS_DIR, 'section-connect.svg'), section_connect_svg)

# ═══════════════════════════════════════════════════════════════
# 9. CONNECT CHIPS (3 chips: 293+294+293 = 880px Solid Dark Tiled Bar)
# ═══════════════════════════════════════════════════════════════
chips_data = [
    ('resume',    293, '📄 View Resume (PDF)', NEON_GREEN, True),
    ('linkedin',  294, '💼 LinkedIn Profile',  NEON_CYAN,  False),
    ('portfolio', 293, '🌐 Personal Portfolio', NEON_GREEN, False),
]

for c_id, w, label, color, has_left_margin in chips_data:
    left_line = f"""
      <line x1="45" y1="0" x2="45" y2="54" stroke="{NEON_GREEN}" stroke-width="1.2" opacity="0.35"/>
      <line x1="49" y1="0" x2="49" y2="54" stroke="{NEON_CYAN}" stroke-width="0.6" opacity="0.2"/>
    """ if has_left_margin else ""

    chip_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 54" width="{w}" height="54">
  <defs>
    {COMMON_DEFS}
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

  <!-- Full-bleed dark background tiles seamlessly into 880px container -->
  <rect width="{w}" height="54" fill="{BG}"/>
  <rect width="{w}" height="54" fill="url(#notebookGrid)"/>
  {left_line}

  <!-- Centered Chip Pill -->
  <rect x="{(w-210)//2}" y="6" width="210" height="42" rx="21" fill="{BG_SURFACE}" stroke="{color}" stroke-width="1.5" filter="url(#chipGlow_{c_id})"/>
  <text x="{w//2}" y="32" text-anchor="middle" class="doodle-hand" font-size="17" font-weight="700" fill="{TEXT_MAIN}">{label}</text>
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
# 11. README.md - 100% ZERO HORIZONTAL WHITE LINES!
# ═══════════════════════════════════════════════════════════════
readme_md = f"""<div align="center">
  <img src="./assets/hero-banner.svg" alt="Hey, I'm Parmeet — Full-Stack Developer" width="100%" align="top" /><!--
  --><a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-resume.svg" width="25%" align="top" alt="View Resume (PDF)" /></a><!--
  --><a href="https://personal-portfolio-parmeet1.vercel.app/contact/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-talk.svg" width="25%" align="top" alt="Let's Talk" /></a><!--
  --><a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-linkedin.svg" width="25%" align="top" alt="LinkedIn Profile" /></a><!--
  --><a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/btn-portfolio.svg" width="25%" align="top" alt="Personal Portfolio" /></a><!--
  --><img src="./assets/tech-stack.svg" alt="Tech Stack &amp; Toolkit: React, Next.js, Python, Django, Node.js" width="100%" align="top" /><!--
  --><img src="./assets/section-work.svg" alt="Featured Projects — Click any card to launch demo" width="100%" align="top" /><!--
  --><a href="https://tradelab-kappa.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-01-tradelab.svg" width="50%" align="top" alt="TradeLab — Real-Time Stock Market Simulator (Launch Demo)" /></a><!--
  --><a href="https://tour-craze.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-02-tourcraze.svg" width="50%" align="top" alt="TourCraze — AI Travel Planning Platform (Launch Demo)" /></a><!--
  --><a href="https://car-trade-gamma.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-03-gaadimandi.svg" width="50%" align="top" alt="GaadiMandi — Vehicle Marketplace (Launch Demo)" /></a><!--
  --><a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/card-04-portfolio.svg" width="50%" align="top" alt="Personal Portfolio 2026 (Launch Live Site)" /></a><!--
  --><img src="./assets/section-connect.svg" alt="Let's Connect &amp; Build" width="100%" align="top" /><!--
  --><a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-resume.svg" width="33.33%" align="top" alt="View Resume (PDF)" /></a><!--
  --><a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-linkedin.svg" width="33.34%" align="top" alt="LinkedIn Profile" /></a><!--
  --><a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer"><img src="./assets/chip-portfolio.svg" width="33.33%" align="top" alt="Personal Portfolio" /></a><!--
  --><img src="./assets/footer-bar.svg" alt="Parmeet Singh • Full-Stack Developer • Delhi, India" width="100%" align="top" />
</div>"""

write_file('README.md', readme_md)

# ═══════════════════════════════════════════════════════════════
# 12. PREVIEW HTML (Local Test & Verification)
# ═══════════════════════════════════════════════════════════════
preview_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Parmeet Singh — GitHub Profile Preview (Light &amp; Dark Mode Test)</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      background: #ffffff;
      color: #000;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 16px;
      min-height: 100vh;
      transition: background 0.3s ease;
    }}
    .mode-switch {{
      margin-bottom: 24px;
      display: flex;
      gap: 12px;
    }}
    .mode-btn {{
      padding: 10px 20px;
      border-radius: 20px;
      border: 1px solid #ccc;
      cursor: pointer;
      font-weight: 600;
      font-size: 13px;
      background: #f6f8fa;
    }}
    .github-canvas {{
      max-width: 880px;
      width: 100%;
      text-align: center;
      line-height: 1.5;
      font-size: 16px;
    }}
    .github-canvas img {{
      box-sizing: content-box;
      max-width: 100%;
    }}
    .github-canvas a {{
      text-decoration: none;
    }}
  </style>
</head>
<body>
  <div class="mode-switch">
    <button class="mode-btn" onclick="document.body.style.background='#ffffff';">☀️ Light Mode (#ffffff)</button>
    <button class="mode-btn" onclick="document.body.style.background='#0d1117';">🌙 Dark Mode (#0d1117)</button>
  </div>
  <div class="github-canvas">
    {readme_md}
  </div>
</body>
</html>"""

write_file('preview.html', preview_html)
print("\\nAll profile assets, README.md, and preview.html successfully updated!")
