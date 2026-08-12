# Hero Accent Colour — Options

The homepage hero uses a single accent colour for the **eyebrow** ("Histopathology ·
Molecular Diagnostics") and the **highlighted phrase** in the headline ("your clinicians
can trust").

## How to change it
Edit one line in `css/style.css` (in the Hero section) and refresh:

```css
.hero { --hero-accent: #4DA8FF; }
```

Both the eyebrow and the headline accent update together.

## Shortlist tried

| # | Name      | Hex       |
|---|-----------|-----------|
| 1 | Gold      | `#F5B301` |
| 2 | Cyan      | `#37C6E0` |
| 3 | Teal      | `#35C79A` |
| 4 | Honey     | `#FFC24B` |
| 5 | Coral     | `#FF7A59` |
| 6 | Lavender  | `#B79CFF` |
| 7 | Sky-blue  | `#4DA8FF` | ← **current selection**
| 8 | Mint      | `#6FE3C4` |
| 9 | Lime      | `#C6F04B` |
| 10 | Rose     | `#FF5C7A` |

**Brand magenta** (`#EC008C`) is also available but was set aside for the hero.

## Notes
- Brand palette is navy `#232C8E` + magenta `#EC008C`; these hero accents are
  non-brand experimental options for the hero copy only.
- Once finalised: match the interior **page-hero accent bar** (`.page-hero h1::after`,
  currently magenta) to the chosen colour so the whole site stays consistent.
