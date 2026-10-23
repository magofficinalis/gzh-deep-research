#!/usr/bin/env python3
"""
横纵分析法报告 Markdown → PDF 转换脚本 (Windows / Chrome 无头版)

用途：当系统没有 GTK3 原生库、WeasyPrint 无法加载 libgobject-2.0-0 时使用。
复用 md_to_pdf.py 的封面与 CSS，改用 Chrome/Edge 无头打印渲染，
再用 reportlab 叠加页眉与「第 X 页」页码，视觉效果与原 WeasyPrint 版保持一致。

用法: python md_to_pdf_win.py input.md output.pdf [--title "报告标题"] [--author "作者"]

依赖: pip install markdown reportlab pypdf
"""

import os
import re
import sys
import shutil
import argparse
import subprocess
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from md_to_pdf import md_to_html  # noqa: E402

# A4 尺寸（pt）
A4_W, A4_H = 595.28, 841.89

# Windows 中文字体栈，替换掉 CSS 里仅 Linux 才有的 Droid Sans Fallback
WIN_FONT_STACK = ('"Microsoft YaHei", "微软雅黑", "Source Han Sans SC", '
                  '"PingFang SC", "Segoe UI", sans-serif')

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_browser():
    """定位可用的 Chrome / Edge 可执行文件"""
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    for name in ("chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    return None


def adapt_html_for_windows(html):
    """把 Linux 字体栈换成 Windows 字体栈，并去掉 Chrome 不支持的页眉页脚 margin box"""
    html = html.replace('"Droid Sans Fallback", Helvetica, Arial, sans-serif',
                        WIN_FONT_STACK)
    # Chrome 不支持 CSS Paged Media 的 @top-center / @bottom-center，移除以免干扰
    html = re.sub(r'@top-center\s*\{[^}]*\}', '', html)
    html = re.sub(r'@bottom-center\s*\{[^}]*\}', '', html)
    return html


def print_pdf(browser, html_path, pdf_path):
    """用 Chrome 无头模式把 HTML 打印成 PDF"""
    file_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    abs_pdf = os.path.abspath(pdf_path)
    if os.path.exists(abs_pdf):
        os.remove(abs_pdf)

    profile_dir = tempfile.mkdtemp(prefix="hv_chrome_")
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-first-run",
        "--no-pdf-header-footer",
        f"--user-data-dir={profile_dir}",
        "--virtual-time-budget=8000",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={abs_pdf}",
        file_url,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    shutil.rmtree(profile_dir, ignore_errors=True)

    if not os.path.exists(abs_pdf) or os.path.getsize(abs_pdf) == 0:
        raise RuntimeError(
            "Chrome 未能生成 PDF。\n"
            f"命令: {' '.join(cmd)}\n"
            f"stdout: {proc.stdout[-800:]}\nstderr: {proc.stderr[-800:]}"
        )


def stamp_header_footer(pdf_path, header_text, out_path):
    """为第 2 页起的每页叠加页眉与「第 X 页」页脚"""
    from io import BytesIO
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont

    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        font_name = "STSong-Light"
    except Exception:
        font_name = "Helvetica"

    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    total = len(reader.pages)

    for idx, page in enumerate(reader.pages):
        if idx > 0:  # 封面不显示页眉页码
            buf = BytesIO()
            c = canvas.Canvas(buf, pagesize=(A4_W, A4_H))
            c.setFont(font_name, 8)

            # 页眉：文字 + 下划线
            c.setFillColorRGB(0.584, 0.647, 0.651)  # #95a5a6
            c.drawCentredString(A4_W / 2, A4_H - 46, header_text)
            c.setStrokeColorRGB(0.925, 0.941, 0.945)  # #ecf0f1
            c.setLineWidth(0.5)
            c.line(56.69, A4_H - 54, A4_W - 56.69, A4_H - 54)

            # 页脚：上划线 + 页码
            c.setStrokeColorRGB(0.102, 0.322, 0.463)  # #1a5276
            c.setLineWidth(0.8)
            c.line(56.69, 40, A4_W - 56.69, 40)
            c.setFillColorRGB(0.584, 0.647, 0.651)
            c.drawCentredString(A4_W / 2, 28, f"第 {idx + 1} 页")

            c.save()
            buf.seek(0)
            overlay = PdfReader(buf).pages[0]
            page.merge_page(overlay)

        writer.add_page(page)

    with open(out_path, "wb") as f:
        writer.write(f)
    return total


def main():
    parser = argparse.ArgumentParser(description="横纵分析法报告 Markdown → PDF (Windows/Chrome)")
    parser.add_argument("input", help="输入的 Markdown 文件路径")
    parser.add_argument("output", help="输出的 PDF 文件路径")
    parser.add_argument("--title", default=None, help="报告标题")
    parser.add_argument("--author", default="数字生命卡兹克", help="作者名")
    args = parser.parse_args()

    browser = find_browser()
    if not browser:
        sys.exit("[ERROR] 未找到 Chrome 或 Edge，无法渲染 PDF")

    with open(args.input, "r", encoding="utf-8") as f:
        md_text = f.read()

    meta_line = ""
    for line in md_text.split("\n"):
        stripped = line.strip().lstrip(">").strip()
        if "研究时间" in stripped or "所属领域" in stripped or "研究对象类型" in stripped:
            meta_line = stripped
            break

    html = md_to_html(md_text, title=args.title or "横纵分析报告",
                      meta_line=meta_line, author=args.author)
    html = adapt_html_for_windows(html)

    html_path = args.output.replace(".pdf", ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] HTML 已生成: {html_path}")

    raw_pdf = args.output.replace(".pdf", "_raw.pdf")
    print(f"[..] 使用 {os.path.basename(browser)} 渲染 PDF")
    print_pdf(browser, html_path, raw_pdf)

    title = args.title or "横纵分析报告"
    header = f"{title}  |  横纵分析法深度研究报告"
    pages = stamp_header_footer(raw_pdf, header, args.output)
    try:
        os.remove(raw_pdf)
    except OSError:
        pass

    size_kb = os.path.getsize(args.output) / 1024
    print(f"[OK] PDF 已生成: {args.output} ({pages} 页, {size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
