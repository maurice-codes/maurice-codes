"""Generates assets/study-progress.svg showing the progress of the study programme."""
from datetime import date
from pathlib import Path

START = date(2023, 10, 1)
END = date(2027, 3, 31)

BAR_X, BAR_Y, BAR_W, BAR_H = 20, 52, 560, 22


def main() -> None:
    today = date.today()
    total = (END - START).days
    elapsed = (today - START).days
    pct = max(0.0, min(1.0, elapsed / total))
    fill_w = round(BAR_W * pct, 1)
    pct_text = f"{pct * 100:.1f}%"
    days_left = max(0, (END - today).days)
    status = "Completed 🎓" if pct >= 1 else f"{days_left} days to go"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="110" viewBox="0 0 600 110">
  <defs>
    <linearGradient id="fill" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0%" stop-color="#A7D8FF"/>
      <stop offset="100%" stop-color="#5AB4F0"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="barClip">
      <rect x="{BAR_X}" y="{BAR_Y}" width="{fill_w}" height="{BAR_H}" rx="11">
        <animate attributeName="width" from="0" to="{fill_w}" dur="1.8s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1" keyTimes="0;1"/>
      </rect>
    </clipPath>
  </defs>

  <style>
    .title {{ font: 600 16px 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; fill: #5AB4F0; }}
    .pct   {{ font: 700 16px 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; fill: #5AB4F0; }}
    .small {{ font: 400 12px 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; fill: #8AA4B8; }}
    .fade  {{ opacity: 0; animation: fadeIn 0.8s ease-out 1.2s forwards; }}
    @keyframes fadeIn {{ to {{ opacity: 1; }} }}
  </style>

  <text x="{BAR_X}" y="36" class="title">🎓 B.Sc. Computer Science</text>
  <text x="{BAR_X + BAR_W}" y="36" class="pct fade" text-anchor="end">{pct_text}</text>

  <rect x="{BAR_X}" y="{BAR_Y}" width="{BAR_W}" height="{BAR_H}" rx="11" fill="#E0F4FF"/>
  <g clip-path="url(#barClip)">
    <rect x="{BAR_X}" y="{BAR_Y}" width="{BAR_W}" height="{BAR_H}" fill="url(#fill)"/>
    <rect x="-120" y="{BAR_Y}" width="120" height="{BAR_H}" fill="url(#shine)">
      <animate attributeName="x" from="-120" to="{BAR_X + BAR_W}" dur="2.5s" begin="1.8s" repeatCount="indefinite"/>
    </rect>
  </g>

  <text x="{BAR_X}" y="96" class="small">01.10.2023</text>
  <text x="300" y="96" class="small fade" text-anchor="middle">{status}</text>
  <text x="{BAR_X + BAR_W}" y="96" class="small" text-anchor="end">31.03.2027</text>
</svg>
"""
    out = Path("assets/study-progress.svg")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    print(f"Progress: {pct_text} ({status})")


if __name__ == "__main__":
    main()
