#!/usr/bin/env python3
"""
build_profile.py — Generates Parmeet's neon-themed GitHub profile.
Creates all SVG assets + README.md + preview.html
"""

import base64, os, textwrap

# ═══════════════════════════════════════════════════════════════
# DESIGN TOKENS
# ═══════════════════════════════════════════════════════════════
BG       = '#0d1117'
BG_CARD  = '#161b22'
NEON     = '#39FF14'
MINT     = '#98FFB8'
DIM_NEON = '#1a3a1a'
WHITE    = '#e6edf3'
GRAY     = '#8b949e'
DIM      = '#484f58'
FONT     = "'Segoe UI', system-ui, -apple-system, sans-serif"
MONO     = "'Consolas', 'SF Mono', 'Fira Code', monospace"
ASSETS   = 'assets'

os.makedirs(ASSETS, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# READ AVATAR → BASE64
# ═══════════════════════════════════════════════════════════════
with open(f'{ASSETS}/parmeet-avatar.png', 'rb') as f:
    AVATAR_B64 = base64.b64encode(f.read()).decode()
print(f'[OK] Avatar loaded ({len(AVATAR_B64)//1024}KB base64)')

# ═══════════════════════════════════════════════════════════════
# HELPER: WRITE FILE
# ═══════════════════════════════════════════════════════════════
def write(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f'[OK] {path}')

# ═══════════════════════════════════════════════════════════════
# COMMON SVG FRAGMENTS
# ═══════════════════════════════════════════════════════════════
DOT_PATTERN = f'''<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="12" cy="12" r="0.5" fill="{DIM_NEON}" opacity="0.5"/>
    </pattern>'''

NEON_GLOW = f'''<filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>
      <feFlood flood-color="{NEON}" flood-opacity="0.5" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="g"/>
      <feMerge>
        <feMergeNode in="g"/>
        <feMergeNode in="g"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>'''

def bg(w, h):
    return f'''<rect width="{w}" height="{h}" fill="{BG}"/>
  <rect width="{w}" height="{h}" fill="url(#dots)"/>'''

# ═══════════════════════════════════════════════════════════════
# 1. HERO BANNER (880 × 340)
# ═══════════════════════════════════════════════════════════════
hero = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 880 340" width="880" height="340">
  <defs>
    {DOT_PATTERN}
    {NEON_GLOW}
    <linearGradient id="topFade" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{NEON}" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="{BG}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="shimmer" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{WHITE}">
        <animate attributeName="stop-color" values="{WHITE};{MINT};{WHITE}" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="{MINT}">
        <animate attributeName="stop-color" values="{MINT};{WHITE};{MINT}" dur="5s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <radialGradient id="avatarGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{NEON}" stop-opacity="0.18"/>
      <stop offset="70%" stop-color="{NEON}" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <style>
    @keyframes float {{ 0%,100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-10px); }} }}
    @keyframes fadeUp {{ from {{ opacity:0; transform:translateY(18px); }} to {{ opacity:1; transform:translateY(0); }} }}
    @keyframes pulse {{ 0%,100% {{ opacity:0.25; }} 50% {{ opacity:0.85; }} }}
    @keyframes lineReveal {{ from {{ stroke-dashoffset:300; }} to {{ stroke-dashoffset:0; }} }}
    @keyframes glowPulse {{ 0%,100% {{ opacity:0.5; }} 50% {{ opacity:1; }} }}
    .float {{ animation: float 4s ease-in-out infinite; }}
    .f1 {{ animation: fadeUp .7s ease .1s both; }}
    .f2 {{ animation: fadeUp .7s ease .35s both; }}
    .f3 {{ animation: fadeUp .7s ease .6s both; }}
    .f4 {{ animation: fadeUp .7s ease .85s both; }}
    .dot {{ animation: pulse 3s ease-in-out infinite; }}
  </style>

  <!-- Background -->
  {bg(880, 340)}
  <rect width="880" height="150" fill="url(#topFade)"/>

  <!-- Greeting -->
  <g class="f1">
    <text x="60" y="95" font-family="{FONT}" font-size="20" fill="{GRAY}" letter-spacing="0.3">Hey there! I am</text>
  </g>

  <!-- Name -->
  <g class="f2">
    <text x="58" y="155" font-family="{FONT}" font-size="54" font-weight="800" fill="url(#shimmer)" letter-spacing="-1">Parmeet Singh</text>
  </g>

  <!-- Neon underline -->
  <line x1="60" y1="172" x2="360" y2="172" stroke="{NEON}" stroke-width="2.5" stroke-dasharray="300" opacity="0.7" filter="url(#glow)">
    <animate attributeName="stroke-dashoffset" from="300" to="0" dur="1.2s" fill="freeze" begin="0.5s"/>
    <animate attributeName="opacity" values="0.5;0.9;0.5" dur="3s" repeatCount="indefinite" begin="1.7s"/>
  </line>

  <!-- Role -->
  <g class="f3">
    <text x="62" y="210" font-family="{MONO}" font-size="15" fill="{MINT}" letter-spacing="1.5" opacity="0.9">Full-Stack Developer</text>
    <text x="62" y="234" font-family="{MONO}" font-size="13" fill="{MINT}" letter-spacing="1.2" opacity="0.55">Web  ·  Data  ·  AI</text>
  </g>

  <!-- Tagline -->
  <g class="f4">
    <text x="62" y="278" font-family="{FONT}" font-size="13" fill="{GRAY}" opacity="0.65">I build things that live on the internet — and sometimes</text>
    <text x="62" y="296" font-family="{FONT}" font-size="13" fill="{GRAY}" opacity="0.65">they are actually useful.</text>
  </g>

  <!-- Floating Avatar Group -->
  <g class="float" transform-origin="720 160">
    <ellipse cx="720" cy="175" rx="125" ry="150" fill="url(#avatarGlow)"/>
    <image href="data:image/png;base64,{AVATAR_B64}"
           x="608" y="18" width="225" height="305"
           preserveAspectRatio="xMidYMid meet"/>
  </g>

  <!-- Decorative particles -->
  <circle cx="625" cy="55" r="2.2" fill="{NEON}" class="dot"/>
  <circle cx="815" cy="80" r="1.6" fill="{MINT}" class="dot" style="animation-delay:.6s"/>
  <circle cx="805" cy="285" r="2" fill="{NEON}" class="dot" style="animation-delay:1.2s"/>
  <circle cx="638" cy="300" r="1.4" fill="{MINT}" class="dot" style="animation-delay:1.8s"/>
  <circle cx="840" cy="175" r="1.2" fill="{NEON}" class="dot" style="animation-delay:2.2s"/>
  <circle cx="600" cy="170" r="1" fill="{MINT}" class="dot" style="animation-delay:0.9s"/>
</svg>'''

write(f'{ASSETS}/hero-banner.svg', hero)


# ═══════════════════════════════════════════════════════════════
# 2. NEON PILL BUTTONS (individual, clickable)
# ═══════════════════════════════════════════════════════════════
buttons = [
    ('resume',   'View Resume', 148),
    ('linkedin', 'LinkedIn',    118),
    ('talk',     "Let's Talk",  130),
]

for bname, blabel, bw in buttons:
    bsvg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {bw} 40" width="{bw}" height="40">
  <defs>
    <filter id="g" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="b"/>
      <feFlood flood-color="{NEON}" flood-opacity="0.35" result="c"/>
      <feComposite in="c" in2="b" operator="in" result="gl"/>
      <feMerge><feMergeNode in="gl"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect x="1.5" y="1.5" width="{bw-3}" height="37" rx="18.5" fill="{BG_CARD}" stroke="{NEON}" stroke-width="1.5" filter="url(#g)">
    <animate attributeName="stroke-opacity" values="0.55;1;0.55" dur="3s" repeatCount="indefinite"/>
  </rect>
  <text x="{bw//2}" y="25" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="600" fill="{WHITE}">{blabel}</text>
</svg>'''
    write(f'{ASSETS}/btn-{bname}.svg', bsvg)


# ═══════════════════════════════════════════════════════════════
# 3. TECH STACK (880 × 150)
# ═══════════════════════════════════════════════════════════════
techs = ['React', 'Next.js', 'Node.js', 'Python', 'Django', 'MongoDB', 'Tailwind']
char_w = 7.8
pad = 28
gap = 14
pills_data = [(t, int(len(t)*char_w + pad)) for t in techs]
total_w = sum(w for _,w in pills_data) + gap*(len(pills_data)-1)
sx = (880 - total_w) / 2

pill_rects = []
pill_texts = []
x = sx
for i, (t, w) in enumerate(pills_data):
    delay = 0.1 * i
    pill_rects.append(
        f'<rect x="{x:.0f}" y="88" width="{w}" height="30" rx="15" '
        f'fill="{BG_CARD}" stroke="{NEON}" stroke-width="1" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="0.85" dur="0.5s" begin="{delay:.1f}s" fill="freeze"/>'
        f'<animate attributeName="stroke-opacity" values="0.4;0.9;0.4" dur="3s" begin="{delay+0.5:.1f}s" repeatCount="indefinite"/>'
        f'</rect>')
    pill_texts.append(
        f'<text x="{x + w/2:.0f}" y="108" text-anchor="middle" '
        f'font-family="{MONO}" font-size="12" fill="{WHITE}" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="{delay:.1f}s" fill="freeze"/>'
        f'{t}</text>')
    x += w + gap

# second row — more techs
techs2 = ['JavaScript', 'Express', 'PostgreSQL', 'Git', 'REST APIs']
pills2_data = [(t, int(len(t)*char_w + pad)) for t in techs2]
total_w2 = sum(w for _,w in pills2_data) + gap*(len(pills2_data)-1)
sx2 = (880 - total_w2) / 2

x2 = sx2
for i, (t, w) in enumerate(pills2_data):
    delay = 0.1 * (i + len(techs)) + 0.15
    pill_rects.append(
        f'<rect x="{x2:.0f}" y="132" width="{w}" height="30" rx="15" '
        f'fill="{BG_CARD}" stroke="{NEON}" stroke-width="1" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="0.85" dur="0.5s" begin="{delay:.1f}s" fill="freeze"/>'
        f'<animate attributeName="stroke-opacity" values="0.4;0.9;0.4" dur="3s" begin="{delay+0.5:.1f}s" repeatCount="indefinite"/>'
        f'</rect>')
    pill_texts.append(
        f'<text x="{x2 + w/2:.0f}" y="152" text-anchor="middle" '
        f'font-family="{MONO}" font-size="12" fill="{WHITE}" opacity="0">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="{delay:.1f}s" fill="freeze"/>'
        f'{t}</text>')
    x2 += w + gap

tech_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 180" width="880" height="180">
  <defs>
    {DOT_PATTERN}
    {NEON_GLOW}
  </defs>
  {bg(880, 180)}

  <!-- Section title -->
  <text x="440" y="42" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="700" fill="{WHITE}" letter-spacing="3" opacity="0.9">WHAT I BUILD WITH</text>
  <line x1="340" y1="55" x2="540" y2="55" stroke="{NEON}" stroke-width="1.5" opacity="0.5" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;0.7;0.3" dur="3s" repeatCount="indefinite"/>
  </line>

  <!-- Tech pills row 1 -->
  {''.join(pill_rects)}
  {''.join(pill_texts)}
</svg>'''

write(f'{ASSETS}/tech-stack.svg', tech_svg)


# ═══════════════════════════════════════════════════════════════
# 4. SECTION HEADERS
# ═══════════════════════════════════════════════════════════════
work_header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 55" width="880" height="55">
  <defs>
    {DOT_PATTERN}
    {NEON_GLOW}
  </defs>
  {bg(880, 55)}
  <text x="440" y="32" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="700" fill="{WHITE}" letter-spacing="3" opacity="0.9">SELECTED WORK</text>
  <line x1="340" y1="44" x2="540" y2="44" stroke="{NEON}" stroke-width="1.5" opacity="0.5" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;0.7;0.3" dur="3s" repeatCount="indefinite"/>
  </line>
</svg>'''
write(f'{ASSETS}/section-work.svg', work_header)

connect_header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 65" width="880" height="65">
  <defs>
    {DOT_PATTERN}
    {NEON_GLOW}
  </defs>
  {bg(880, 65)}
  <text x="440" y="30" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="700" fill="{WHITE}" letter-spacing="3" opacity="0.9">LET'S CONNECT</text>
  <line x1="345" y1="42" x2="535" y2="42" stroke="{NEON}" stroke-width="1.5" opacity="0.5" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;0.7;0.3" dur="3s" repeatCount="indefinite"/>
  </line>
  <text x="440" y="58" text-anchor="middle" font-family="{FONT}" font-size="12" fill="{GRAY}" opacity="0.6">Always up for a conversation — reach out anytime.</text>
</svg>'''
write(f'{ASSETS}/section-connect.svg', connect_header)


# ═══════════════════════════════════════════════════════════════
# 5. PROJECT CARDS (430 × 170 each)
# ═══════════════════════════════════════════════════════════════
projects = [
    {
        'id': '01', 'name': 'TradeLab', 'file': 'card-01-tradelab',
        'tags': 'React · Node.js · MongoDB',
        'desc1': 'Real-time stock market simulator',
        'desc2': 'with virtual trading & portfolio tracking.',
    },
    {
        'id': '02', 'name': 'TourCraze', 'file': 'card-02-tourcraze',
        'tags': 'React · Express · MongoDB',
        'desc1': 'AI-powered travel planning platform',
        'desc2': 'for discovering and booking curated tours.',
    },
    {
        'id': '03', 'name': 'GaadiMandi', 'file': 'card-03-gaadimandi',
        'tags': 'Python · Django · PostgreSQL',
        'desc1': 'Full-stack vehicle marketplace with',
        'desc2': 'real-time listings, filters & analytics.',
    },
    {
        'id': '04', 'name': 'Portfolio', 'file': 'card-04-portfolio',
        'tags': 'Next.js · Tailwind · Motion',
        'desc1': 'Personal developer portfolio',
        'desc2': 'with interactive project showcases.',
    },
]

for p in projects:
    card = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 170" width="430" height="170">
  <defs>
    {DOT_PATTERN}
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>
      <feFlood flood-color="{NEON}" flood-opacity="0.4" result="color"/>
      <feComposite in="color" in2="blur" operator="in" result="g"/>
      <feMerge><feMergeNode in="g"/><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feFlood flood-color="{NEON}" flood-opacity="0.15"/>
      <feComposite in2="b" operator="in" result="g"/>
      <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <style>
    @keyframes borderGlow {{ 0%,100% {{ opacity:0.45; }} 50% {{ opacity:0.95; }} }}
    .glow-border {{ animation: borderGlow 3s ease-in-out infinite; }}
  </style>

  <!-- Card background -->
  <rect width="430" height="170" rx="12" fill="{BG}"/>
  <rect width="430" height="170" rx="12" fill="url(#dots)" opacity="0.5"/>
  <rect x="1" y="1" width="428" height="168" rx="11" fill="none" stroke="{BG_CARD}" stroke-width="1"/>

  <!-- Neon left accent bar -->
  <rect x="0" y="20" width="3.5" height="130" rx="2" fill="{NEON}" class="glow-border" filter="url(#glow)"/>

  <!-- Project number (large, dim) -->
  <text x="390" y="45" text-anchor="end" font-family="{MONO}" font-size="40" font-weight="800" fill="{DIM_NEON}" opacity="0.5">{p['id']}</text>

  <!-- Project name -->
  <text x="24" y="48" font-family="{FONT}" font-size="22" font-weight="700" fill="{WHITE}">{p['name']}</text>

  <!-- Tech tags -->
  <text x="24" y="72" font-family="{MONO}" font-size="11" fill="{NEON}" opacity="0.7">{p['tags']}</text>

  <!-- Description -->
  <text x="24" y="102" font-family="{FONT}" font-size="13" fill="{GRAY}" opacity="0.75">{p['desc1']}</text>
  <text x="24" y="120" font-family="{FONT}" font-size="13" fill="{GRAY}" opacity="0.75">{p['desc2']}</text>

  <!-- LIVE DEMO link -->
  <text x="24" y="152" font-family="{MONO}" font-size="12" font-weight="700" fill="{NEON}" filter="url(#softGlow)">LIVE DEMO  →</text>
</svg>'''
    write(f'{ASSETS}/{p["file"]}.svg', card)


# ═══════════════════════════════════════════════════════════════
# 6. CONTACT CHIPS (individual, clickable)
# ═══════════════════════════════════════════════════════════════
chips = [
    ('resume',    'Resume',    100),
    ('linkedin',  'LinkedIn',  108),
    ('email',     'Email',     90),
    ('portfolio', 'Portfolio', 112),
]

for cname, clabel, cw in chips:
    chip = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cw} 38" width="{cw}" height="38">
  <defs>
    <filter id="g" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
      <feFlood flood-color="{NEON}" flood-opacity="0.3" result="c"/>
      <feComposite in="c" in2="b" operator="in" result="gl"/>
      <feMerge><feMergeNode in="gl"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect x="1" y="1" width="{cw-2}" height="36" rx="18" fill="{BG_CARD}" stroke="{NEON}" stroke-width="1.2" filter="url(#g)">
    <animate attributeName="stroke-opacity" values="0.45;0.9;0.45" dur="3.5s" repeatCount="indefinite"/>
  </rect>
  <text x="{cw//2}" y="24" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="600" fill="{MINT}">{clabel}</text>
</svg>'''
    write(f'{ASSETS}/chip-{cname}.svg', chip)


# ═══════════════════════════════════════════════════════════════
# 7. FOOTER BAR (880 × 45)
# ═══════════════════════════════════════════════════════════════
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 45" width="880" height="45">
  <defs>
    {DOT_PATTERN}
    {NEON_GLOW}
  </defs>
  {bg(880, 45)}
  <line x1="240" y1="5" x2="640" y2="5" stroke="{DIM_NEON}" stroke-width="0.5" opacity="0.5"/>
  <text x="440" y="30" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{DIM}" letter-spacing="2" opacity="0.6">PARMEET SINGH  ·  FULL-STACK DEVELOPER  ·  DELHI, INDIA</text>
</svg>'''
write(f'{ASSETS}/footer-bar.svg', footer)


# ═══════════════════════════════════════════════════════════════
# 8. README.md
# ═══════════════════════════════════════════════════════════════
readme = '''<div align="center">

  <!-- ═══ HERO BANNER ═══ -->
  <img src="./assets/hero-banner.svg" alt="Hey there! I am Parmeet Singh — Full-Stack Developer" width="100%" style="max-width: 880px; display: block;" />

  <!-- ═══ ACTION BUTTONS ═══ -->
  <p align="center" style="margin: 8px 0 20px;">
    <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer">
      <img src="./assets/btn-resume.svg" height="38" alt="View Resume" />
    </a>
    &nbsp;&nbsp;
    <a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer">
      <img src="./assets/btn-linkedin.svg" height="38" alt="LinkedIn" />
    </a>
    &nbsp;&nbsp;
    <a href="mailto:parmeetssms@gmail.com">
      <img src="./assets/btn-talk.svg" height="38" alt="Let\\'s Talk" />
    </a>
  </p>

  <!-- ═══ TECH STACK ═══ -->
  <img src="./assets/tech-stack.svg" alt="Technologies I build with" width="100%" style="max-width: 880px; display: block;" />

  <!-- ═══ PROJECTS HEADER ═══ -->
  <img src="./assets/section-work.svg" alt="Selected Work" width="100%" style="max-width: 880px; display: block;" />

  <!-- ═══ PROJECT CARDS ROW 1 ═══ -->
  <p align="center" style="margin: 4px 0 0;">
    <a href="https://tradelab-kappa.vercel.app/" target="_blank" rel="noopener noreferrer">
      <img src="./assets/card-01-tradelab.svg" width="48.5%" style="max-width: 430px; margin: 3px;" alt="TradeLab — Live Demo" />
    </a>
    <a href="https://tour-craze.vercel.app/" target="_blank" rel="noopener noreferrer">
      <img src="./assets/card-02-tourcraze.svg" width="48.5%" style="max-width: 430px; margin: 3px;" alt="TourCraze — Live Demo" />
    </a>
  </p>

  <!-- ═══ PROJECT CARDS ROW 2 ═══ -->
  <p align="center" style="margin: 0 0 4px;">
    <a href="https://car-trade-gamma.vercel.app/" target="_blank" rel="noopener noreferrer">
      <img src="./assets/card-03-gaadimandi.svg" width="48.5%" style="max-width: 430px; margin: 3px;" alt="GaadiMandi — Live Demo" />
    </a>
    <a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer">
      <img src="./assets/card-04-portfolio.svg" width="48.5%" style="max-width: 430px; margin: 3px;" alt="Portfolio — Live Site" />
    </a>
  </p>

  <!-- ═══ QUICK LINKS ═══ -->
  <p align="center" style="margin: 2px 0 16px; font-size: 11px;">
    <a href="https://github.com/singhparmeet12/TradeLab" target="_blank"><code>TradeLab Repo ↗</code></a> &nbsp;·&nbsp;
    <a href="https://github.com/singhparmeet12/TourCraze" target="_blank"><code>TourCraze Repo ↗</code></a> &nbsp;·&nbsp;
    <a href="https://github.com/singhparmeet12/carTrade" target="_blank"><code>GaadiMandi Repo ↗</code></a> &nbsp;·&nbsp;
    <a href="https://github.com/singhparmeet12/portfolio" target="_blank"><code>Portfolio Repo ↗</code></a>
  </p>

  <!-- ═══ CONNECT SECTION ═══ -->
  <img src="./assets/section-connect.svg" alt="Let's Connect" width="100%" style="max-width: 880px; display: block;" />

  <!-- ═══ CONTACT CHIPS ═══ -->
  <p align="center" style="margin: 6px 0 10px;">
    <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank" rel="noopener noreferrer">
      <img src="./assets/chip-resume.svg" height="36" alt="Resume" />
    </a>
    &nbsp;&nbsp;
    <a href="https://linkedin.com/in/parmeetsingh12" target="_blank" rel="noopener noreferrer">
      <img src="./assets/chip-linkedin.svg" height="36" alt="LinkedIn" />
    </a>
    &nbsp;&nbsp;
    <a href="mailto:parmeetssms@gmail.com">
      <img src="./assets/chip-email.svg" height="36" alt="Email" />
    </a>
    &nbsp;&nbsp;
    <a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank" rel="noopener noreferrer">
      <img src="./assets/chip-portfolio.svg" height="36" alt="Portfolio" />
    </a>
  </p>

  <!-- ═══ FOOTER ═══ -->
  <img src="./assets/footer-bar.svg" alt="Parmeet Singh · Full-Stack Developer · Delhi, India" width="100%" style="max-width: 880px; display: block;" />

</div>
'''

write('README.md', readme)


# ═══════════════════════════════════════════════════════════════
# 9. PREVIEW.HTML (local testing)
# ═══════════════════════════════════════════════════════════════
preview = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Parmeet Singh — GitHub Profile Preview</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      background: {BG};
      font-family: {FONT};
      display: flex;
      justify-content: center;
      padding: 32px 16px;
      min-height: 100vh;
    }}
    .container {{
      max-width: 880px;
      width: 100%;
      text-align: center;
    }}
    .container img {{
      display: block;
      margin: 0 auto;
      max-width: 100%;
    }}
    .btn-row {{
      display: flex;
      justify-content: center;
      gap: 12px;
      margin: 8px 0 20px;
      flex-wrap: wrap;
    }}
    .btn-row a img {{
      height: 38px;
      display: inline-block;
    }}
    .cards-row {{
      display: flex;
      justify-content: center;
      gap: 6px;
      margin: 4px 0;
      flex-wrap: wrap;
    }}
    .cards-row a {{
      width: 48.5%;
      max-width: 430px;
    }}
    .cards-row a img {{
      width: 100%;
    }}
    .quick-links {{
      margin: 2px 0 16px;
      font-size: 11px;
      font-family: {MONO};
    }}
    .quick-links a {{
      color: {GRAY};
      text-decoration: none;
    }}
    .quick-links a:hover {{
      color: {NEON};
    }}
    .chip-row {{
      display: flex;
      justify-content: center;
      gap: 10px;
      margin: 6px 0 10px;
      flex-wrap: wrap;
    }}
    .chip-row a img {{
      height: 36px;
      display: inline-block;
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- Hero -->
    <img src="./assets/hero-banner.svg" alt="Hero Banner"/>

    <!-- Buttons -->
    <div class="btn-row">
      <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank">
        <img src="./assets/btn-resume.svg" alt="Resume"/>
      </a>
      <a href="https://linkedin.com/in/parmeetsingh12" target="_blank">
        <img src="./assets/btn-linkedin.svg" alt="LinkedIn"/>
      </a>
      <a href="mailto:parmeetssms@gmail.com">
        <img src="./assets/btn-talk.svg" alt="Let's Talk"/>
      </a>
    </div>

    <!-- Tech Stack -->
    <img src="./assets/tech-stack.svg" alt="Tech Stack"/>

    <!-- Projects Header -->
    <img src="./assets/section-work.svg" alt="Selected Work"/>

    <!-- Cards Row 1 -->
    <div class="cards-row">
      <a href="https://tradelab-kappa.vercel.app/" target="_blank">
        <img src="./assets/card-01-tradelab.svg" alt="TradeLab"/>
      </a>
      <a href="https://tour-craze.vercel.app/" target="_blank">
        <img src="./assets/card-02-tourcraze.svg" alt="TourCraze"/>
      </a>
    </div>

    <!-- Cards Row 2 -->
    <div class="cards-row">
      <a href="https://car-trade-gamma.vercel.app/" target="_blank">
        <img src="./assets/card-03-gaadimandi.svg" alt="GaadiMandi"/>
      </a>
      <a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank">
        <img src="./assets/card-04-portfolio.svg" alt="Portfolio"/>
      </a>
    </div>

    <!-- Quick Links -->
    <div class="quick-links">
      <a href="https://github.com/singhparmeet12/TradeLab">TradeLab Repo ↗</a> &nbsp;·&nbsp;
      <a href="https://github.com/singhparmeet12/TourCraze">TourCraze Repo ↗</a> &nbsp;·&nbsp;
      <a href="https://github.com/singhparmeet12/carTrade">GaadiMandi Repo ↗</a> &nbsp;·&nbsp;
      <a href="https://github.com/singhparmeet12/portfolio">Portfolio Repo ↗</a>
    </div>

    <!-- Connect Header -->
    <img src="./assets/section-connect.svg" alt="Let's Connect"/>

    <!-- Contact Chips -->
    <div class="chip-row">
      <a href="https://personal-portfolio-parmeet1.vercel.app/resume/download/" target="_blank">
        <img src="./assets/chip-resume.svg" alt="Resume"/>
      </a>
      <a href="https://linkedin.com/in/parmeetsingh12" target="_blank">
        <img src="./assets/chip-linkedin.svg" alt="LinkedIn"/>
      </a>
      <a href="mailto:parmeetssms@gmail.com">
        <img src="./assets/chip-email.svg" alt="Email"/>
      </a>
      <a href="https://personal-portfolio-parmeet1.vercel.app/" target="_blank">
        <img src="./assets/chip-portfolio.svg" alt="Portfolio"/>
      </a>
    </div>

    <!-- Footer -->
    <img src="./assets/footer-bar.svg" alt="Footer"/>
  </div>
</body>
</html>'''

write('preview.html', preview)

print('\n[DONE] All files generated successfully!')
print('   Open preview.html in a browser to preview.')
