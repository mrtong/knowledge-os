from pathlib import Path


class MarkdownWriter:
    def write(self, title, markdown):
        output_dir = Path("knowledge/notion")
        output_dir.mkdir(parents=True, exist_ok=True)

        safe_title = title.replace("/", "-").replace("\\", "-")
        path = output_dir / f"{safe_title}.md"

        path.write_text(markdown, encoding="utf-8")
        return path
