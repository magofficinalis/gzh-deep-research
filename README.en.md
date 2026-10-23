# gzh-deep-research

> **Deep research → long-form writing → WeChat Official Account typesetting, all in one Skill.**
>
> Give it a research subject (a product / company / concept / person). It runs web-scale deep research, writes a 10k–30k-character narrative-driven long-form article in Chinese, then typesets it into HTML that pastes into the WeChat Official Account editor **without losing any styling**.

[中文文档](README.md) | English

This is a merged release of two mature Skills:

- **hv-analysis** — Horizontal-Vertical Analysis deep research (methodology by Khazix / 数字生命卡兹克)
- **gzh-design** — a WeChat Official Account typesetting engine with a theme component library

## Preview

A real run: deep research on "Self-Evolving AI", typeset with the **Graphite Minimal** theme ([full page online](https://www.workbuddy.cn/space/d/TlgxosyrlGSRJQ84wHu1zm)).

| Opening: intro card + reading-time line | Vertical analysis: narrative + arXiv figures |
| :---: | :---: |
| ![Opening](docs/images/prev_p1.jpg) | ![Vertical analysis](docs/images/prev_p2.jpg) |

| Horizontal comparison: rivals + charts | Closing & references appendix |
| :---: | :---: |
| ![Horizontal comparison](docs/images/prev_p3.jpg) | ![Closing and sources](docs/images/prev_p4.jpg) |

## What it does

One invocation, four stages:

```
Confirm the research subject
  → Phase 1  Web research (parallel sub-agents: vertical / horizontal / supplementary;
             arXiv is mandatory for academic subjects)
  → Vertical analysis (6k–15k chars: origin, evolution, decision logic, stage division)
  → Horizontal analysis (3k–10k chars: competitive landscape, real user voices)
  → Cross-axis insights (1.5k–3k chars: historical roots of strengths/weaknesses
             + three future scenarios)
  → Output: [subject]_deep-research.md (optional PDF report)
  → Phase 2  Pick a theme → assemble from component library → lint until 0 errors
  → Output: WeChat-ready HTML + one-click-copy preview page
```

### Phase 1: Horizontal-Vertical Analysis research & writing

- **Vertical (time depth)**: the full story from birth to today — every key node reconstructed with *why* the decision was made, not a chronology dump
- **Horizontal (breadth at the present moment)**: systematic comparison with 3–5 representative rivals, quoting real user voices from GitHub Issues / Reddit / Zhihu
- **Cross-axis insights**: how history shaped today's competitive position; which past decisions explain today's strengths and weaknesses; most-likely / most-dangerous / most-optimistic future scenarios
- **Writing style**: rhythm, narrative drive, layered reveals, opinionated but fact-backed, echoing callbacks; a built-in "AI-flavor blacklist" (limited em-dashes, no buzzwords, honest "information unavailable" instead of fabrication)
- **Figures**: first-party images only (arXiv paper figures, official site screenshots), each visually verified, with uniform captions
- **Sources**: every key fact cited, full source list at the end

### Phase 2: WeChat Official Account typesetting

- **6 built-in themes**: Moyu Green, Red-White, Graphite Minimal, Zen Whitespace, Moyu Ticket, Olive Journal — auto-recommended by genre; custom theme generation supported
- **Paste-proof styling**: fully inline styles + `<span leaf="">` wrapping, avoiding the editor's red lines (no `<div>` / `<style>` / class / absolute positioning / grid)
- **Smart enhancements**: auto section numbering (01 / 02 / ∞), English labels, keyword underlines, 3 highlight takeaways, word count & reading time line
- **Mandatory lint**: `validate_gzh_html.py` deterministically checks platform compliance — delivery only at 0 errors / 0 warnings
- **One-click copy preview page**: open in browser → click "Copy to WeChat" → Ctrl+V in the editor

## Repository layout

```
gzh-deep-research/
├── SKILL.md                  # Main pipeline: Phase 1 research & writing → Phase 2 typesetting
├── scripts/
│   ├── md_to_pdf_win.py      # PDF on Windows (Chrome headless + reportlab)
│   ├── md_to_pdf.py          # PDF on Linux/macOS (WeasyPrint)
│   ├── validate_gzh_html.py  # WeChat HTML compliance lint (must reach 0 errors)
│   ├── wrap_preview.py       # Builds the preview page with a copy button
│   ├── component_lint.py     # Theme component library lint
│   └── extract_docx.py       # docx → Markdown extraction
├── references/               # Theme component libraries (theme-index.md is the source of truth)
│   ├── theme-index.md
│   ├── theme-moyu-green.md / theme-red-white.md / theme-graphite-minimal.md / ...
│   ├── common-components.md  # Shared blocks (code / images / tag headings)
│   ├── format-normalize.md   # Non-Markdown input normalization
│   ├── theme-generator.md    # Custom theme generation flow
│   └── eval-cases.md
└── docs/images/              # README preview images
```

## Install & use

In an agent environment that supports Skills (e.g. [WorkBuddy](https://www.workbuddy.cn)), clone into the user-level skills directory:

```bash
git clone https://github.com/magofficinalis/gzh-deep-research ~/.workbuddy/skills/gzh-deep-research
```

> The SKILL.md format is also natively readable by Claude Code — copy the folder into `~/.claude/skills/` instead.

Then just say:

> Deep-research XX for me, write it up as a WeChat article and typeset it

Deliverables:

1. `[subject]_deep-research.md` — the long-form article (10k–30k chars)
2. `[subject]_…_{theme}.html` — clean WeChat-ready body HTML
3. `{...}_preview.html` — preview page with a one-click copy button
4. `[subject]_deep-research.pdf` — optional, beautifully typeset PDF report

**Note**: the writing guidelines and typesetting rules are optimized for Chinese-language output and the WeChat Official Account platform.

## When to use / not use

**Use it for**: systematic deep research on a product / company / concept / person that should end up as a published WeChat article; competitive analysis turned into a post; "research XX and typeset it for my Official Account".

**Not for**: typesetting an existing article only (use gzh-design); research without WeChat output (use hv-analysis); quick term explanations.

## Credits

- Horizontal-Vertical Analysis methodology & writing style guide: Khazix (数字生命卡兹克)
- Typesetting engine: the gzh-design theme component library system
