# gzh-deep-research

公众号深度研究一条龙 Skill：**横纵分析法研究写作（hv-analysis）+ 公众号排版（gzh-design）合并版**。

输入一个研究对象（产品 / 公司 / 概念 / 人物），自动完成：

1. **联网深度研究**（横纵分析法：纵向追时间深度，横向追同期广度，横纵交汇产出洞察）
2. **写出一篇 1–3 万字公众号深度长文**（叙事驱动、敢下判断、官方一手配图、信息来源可考）
3. **排版成公众号 HTML**（主题组件库、粘贴不丢样式、带「一键复制」预览页、校验脚本清零）
4. **可选 PDF 研究报告**（封面 + 页眉页码，Windows / Linux / macOS 双脚本）

## 目录结构

```
gzh-deep-research/
├── SKILL.md                  # 主流程：Phase 1 研究写作 → Phase 2 公众号排版
├── scripts/
│   ├── md_to_pdf_win.py      # Windows PDF 转换（Chrome headless + reportlab）
│   ├── md_to_pdf.py          # Linux/macOS PDF 转换（WeasyPrint）
│   ├── validate_gzh_html.py  # 公众号 HTML 合规校验（必须 0 ERROR）
│   ├── wrap_preview.py       # 生成带「复制到公众号」按钮的预览页
│   ├── component_lint.py     # 主题组件库 lint
│   └── extract_docx.py       # docx → Markdown 抽取
└── references/               # 主题组件库（theme-index.md 为单一来源）
    ├── theme-index.md
    ├── theme-moyu-green.md / theme-red-white.md / theme-graphite-minimal.md / ...
    ├── common-components.md  # 通用增量库（代码块/图片/小标签）
    ├── format-normalize.md   # 非 Markdown 输入归一化
    ├── theme-generator.md    # 自定义主题生成流程
    └── eval-cases.md
```

## 使用

在支持 Skill 的 Agent 环境（如 WorkBuddy）中安装到 `~/.workbuddy/skills/`，然后说：

> 帮我深度研究一下 XX，写成公众号文章并排好版

触发后会依次执行研究写作与排版，最终交付 Markdown 原稿 + 排版 HTML + 预览页（可选 PDF）。

## 致谢

方法论与写作风格源自数字生命卡兹克（Khazix）的横纵分析法；排版引擎源自 gzh-design 主题组件库体系。
