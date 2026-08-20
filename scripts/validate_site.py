#!/usr/bin/env python3
"""Validate the Paper Route Atlas directory convention and local links."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        for key in ("href", "src"):
            reference = values.get(key)
            if reference:
                self.references.append(reference)


def validate_structure(errors: list[str]) -> None:
    required = [
        ROOT / "index.html",
        ROOT / "assets" / "styles.css",
        ROOT / "assets" / "app.js",
        ROOT / "topics",
    ]
    for item in required:
        if not item.exists():
            errors.append(f"缺少必需路径：{item.relative_to(ROOT)}")

    extra_root_html = [path for path in ROOT.glob("*.html") if path.name != "index.html"]
    for path in extra_root_html:
        errors.append(f"根目录不应平铺主题 HTML：{path.name}")

    root_index = (ROOT / "index.html").read_text(encoding="utf-8")
    for topic_dir in sorted((ROOT / "topics").iterdir()):
        if not topic_dir.is_dir():
            continue
        expected_main = topic_dir / f"{topic_dir.name}.html"
        if not expected_main.exists():
            errors.append(
                f"主题主页面必须与目录同名：缺少 {expected_main.relative_to(ROOT)}"
            )
        expected_link = expected_main.relative_to(ROOT).as_posix()
        if expected_link not in root_index:
            errors.append(f"根目录 index.html 未链接主题：{expected_link}")


def validate_pages(errors: list[str]) -> None:
    for page in sorted(ROOT.rglob("*.html")):
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for reference in parser.references:
            if reference.startswith("#"):
                if reference[1:] not in parser.ids:
                    errors.append(f"{page.relative_to(ROOT)} 缺少锚点 {reference}")
                continue

            parsed = urlparse(reference)
            if parsed.scheme or reference.startswith("//"):
                continue
            target = (page.parent / parsed.path).resolve()
            if not target.exists():
                errors.append(
                    f"{page.relative_to(ROOT)} 的本地链接无效：{reference}"
                )


def validate_sources(errors: list[str]) -> None:
    for pdf in sorted(ROOT.rglob("*.pdf")):
        if pdf.stat().st_size < 5:
            errors.append(f"PDF 文件为空或不完整：{pdf.relative_to(ROOT)}")
            continue
        with pdf.open("rb") as stream:
            if stream.read(5) != b"%PDF-":
                errors.append(f"文件不是有效 PDF：{pdf.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    validate_structure(errors)
    validate_pages(errors)
    validate_sources(errors)

    if errors:
        print("验证失败：")
        for error in errors:
            print(f"- {error}")
        return 1

    page_count = sum(1 for _ in ROOT.rglob("*.html"))
    topic_count = sum(1 for path in (ROOT / "topics").iterdir() if path.is_dir())
    pdf_count = sum(1 for _ in ROOT.rglob("*.pdf"))
    print(
        f"验证通过：{topic_count} 个主题，{page_count} 个 HTML，{pdf_count} 份 PDF。"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
