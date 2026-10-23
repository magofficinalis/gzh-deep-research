# gzh-deep-research

> **深度研究 → 长文写作 → 公众号排版，一个 Skill 全包。**
>
> 输入一个研究对象（产品 / 公司 / 概念 / 人物），自动完成联网深度调研，写出一篇 1–3 万字、叙事驱动、敢下判断的深度长文，再排版成可直接粘贴进微信公众号编辑器、样式不丢失的 HTML。

这是两个成熟 Skill 的合并版：

- **[hv-analysis](https://github.com/magofficinalis)** — 横纵分析法深度研究（方法论源自数字生命卡兹克 Khazix）
- **[gzh-design](https://github.com/magofficinalis)** — 公众号文章排版引擎（主题组件库体系）

## 效果预览

以下为一次真实运行的产物节选：对「模型自进化（Self-Evolving AI）」做横纵分析研究后，用**石墨极简风**主题排版出的公众号文章（[在线查看完整页面](https://www.workbuddy.cn/space/d/TlgxosyrlGSRJQ84wHu1zm)）。

| 开头：引言卡 + 章节编号 | 纵向分析：叙事 + arXiv 一手配图 |
| :---: | :---: |
| ![开头与纵向分析](docs/images/shot_1.jpg) | ![横向分析与图表](docs/images/shot_2.jpg) |

| 横向对比：竞品图谱 + 数据图 | 交汇洞察：三剧本推演 + 信息来源 |
| :---: | :---: |
| ![图表与横向对比](docs/images/shot_3.jpg) | ![结尾与信息来源](docs/images/shot_4.jpg) |

在线直链版本：[第 1 段](https://workbuddy-space-static.codebuddy.work/image/TZyMgucHgIraFUDH3sd06Q.jpg) ｜ [第 2 段](https://workbuddy-space-static.codebuddy.work/image/ukN27xjPTxUoosoJB4PsyS.jpg) ｜ [第 3 段](https://workbuddy-space-static.codebuddy.work/image/2Hqf9pVBOF74TUZDPpPuxG.jpg) ｜ [第 4 段](https://workbuddy-space-static.codebuddy.work/image/UqvORRghGLm9myTYAtElhw.jpg)

## 它做什么

一次调用，走完四个阶段：

```
确认研究对象
  → Phase 1 联网研究（并行子 Agent：纵向 / 横向 / 补充信息，学术对象必查 arXiv）
  → 纵向分析（6000–15000 字叙事：起源、演进、决策逻辑、阶段划分）
  → 横向分析（3000–10000 字竞品图谱：场景 A/B/C 分流，含真实用户口碑）
  → 横纵交汇洞察（1500–3000 字：优势/劣势的历史根源 + 未来三剧本推演）
  → 产出 [研究对象]_深度研究.md（可选 PDF 研究报告）
  → Phase 2 选主题 → 组件库装配 → 校验脚本清零
  → 产出公众号排版 HTML + 一键复制预览页
```

### Phase 1：横纵分析法研究写作

- **纵向追时间深度**：完整还原从诞生到当下的发展全貌，每个关键节点还原「为什么选 A 不选 B」的决策逻辑，不是年表流水账
- **横向追同期广度**：以当前时间切面与 3–5 个代表性竞品系统对比，引用 GitHub Issues / Reddit / 知乎等真实用户声音
- **横纵交汇**：历史如何塑造当下竞争位置，优势与劣势各自能追溯到哪个历史决策，最可能 / 最危险 / 最乐观三个未来剧本
- **写作风格**：节奏感、叙事驱动、层层剥开、敢下判断但标注主观性、回环呼应；内置完整「AI 味禁区」清单（破折号限量、禁用「赋能/抓手/综上所述」、搜不到就标「暂缺」绝不编造）
- **配图规范**：只用官方一手图（arXiv 论文插图、官网截图），逐张目检，统一「图 N｜解读。来源：…」题注
- **信息来源**：全文关键事实标注出处，文末完整来源清单

### Phase 2：公众号排版

- **6 套内置主题**：摸鱼绿、红白色系、石墨极简风、留白禅意风、摸鱼票据风、橄榄手记，按题材自动推荐；支持自定义主题生成
- **粘贴不丢样式**：全部内联样式 + `<span leaf="">` 包裹，规避公众号编辑器红线（无 `<div>`/`<style>`/class/绝对定位/Grid）
- **智能增强**：章节自动编号 01/02/∞、英文标签、关键词下划线标记、导读三看点、字数与阅读时间行
- **强制校验**：`validate_gzh_html.py` 确定性检查，0 ERROR 0 WARNING 才交付
- **一键复制预览页**：浏览器打开 → 点「复制到公众号」→ 编辑器里 Ctrl+V 即可

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
├── references/               # 主题组件库（theme-index.md 为单一来源）
│   ├── theme-index.md
│   ├── theme-moyu-green.md / theme-red-white.md / theme-graphite-minimal.md / ...
│   ├── common-components.md  # 通用增量库（代码块 / 图片 / 小标签）
│   ├── format-normalize.md   # 非 Markdown 输入归一化
│   ├── theme-generator.md    # 自定义主题生成流程
│   └── eval-cases.md
└── docs/images/              # README 效果预览图
```

## 安装与使用

在支持 Skill 的 Agent 环境（如 [WorkBuddy](https://www.workbuddy.cn)）中，把本仓库克隆到用户级 Skill 目录：

```bash
git clone https://github.com/magofficinalis/gzh-deep-research ~/.workbuddy/skills/gzh-deep-research
```

然后对 Agent 说：

> 帮我深度研究一下 XX，写成公众号文章并排好版

触发后自动走完研究、写作、排版全流程，最终交付：

1. `[研究对象]_深度研究.md` — 研究长文原稿（1–3 万字）
2. `[研究对象]_深度研究_排版_{主题}.html` — 公众号排版正文（粘贴用）
3. `{...}_预览.html` — 带「一键复制」按钮的预览页
4. `[研究对象]_深度研究.pdf` — 可选，排版精美的 PDF 研究报告（封面 + 页眉页码）

## 适用与不适用

**适用**：产品 / 公司 / 概念 / 技术 / 人物的系统性深度研究并直接发公众号；竞品分析写成推文；「帮我研究 XX 顺便排成公众号文章」。

**不适用**：只排版已有文章（用 gzh-design）；只做研究不出公众号产物（用 hv-analysis）；简单名词解释。

## 致谢

- 横纵分析法与写作风格指南：数字生命卡兹克（Khazix）
- 排版引擎：gzh-design 主题组件库体系
