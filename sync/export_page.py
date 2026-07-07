import sys
from pathlib import Path

from sync.notion_client import NotionClient


def rich_text_text(rich_text, client=None):
    parts = []

    for t in rich_text:
        if t.get("type") == "mention":
            mention = t.get("mention", {})

            if mention.get("type") == "page":
                page_id = mention.get("page", {}).get("id")

                if client and page_id:
                    try:
                        page = client.get_page(page_id)
                        title = get_page_title(page)
                    except Exception:
                        title = t.get("plain_text", "").strip()
                else:
                    title = t.get("plain_text", "").strip()

                parts.append(f"[[{title}]]")
            else:
                parts.append(t.get("plain_text", ""))
        else:
            parts.append(t.get("plain_text", ""))

    return "".join(parts)


def block_to_markdown(block, client):
    block_type = block.get("type")
    content = block.get(block_type, {})

    text = rich_text_text(content.get("rich_text", []), client)

    if block_type == "paragraph":
        return text

    if block_type == "heading_1":
        return f"# {text}"

    if block_type == "heading_2":
        return f"## {text}"

    if block_type == "heading_3":
        return f"### {text}"

    if block_type == "bulleted_list_item":
        return f"- {text}"

    if block_type == "numbered_list_item":
        return f"1. {text}"

    if block_type == "quote":
        return f"> {text}"

    if block_type == "code":
        language = content.get("language", "")
        return f"```{language}\n{text}\n```"
    if block_type == "child_page":
        title = content.get("title", "Untitled")
        return f"- [[{title}]]"
    return f"<!-- unsupported block: {block_type} -->"


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python -m sync.export_page <page_id>")

    page_id = sys.argv[1]

    client = NotionClient()
    blocks = client.get_block_children(page_id)

    lines = []

    for block in blocks:
        md = block_to_markdown(block, client)
        if md:
            lines.append(md)

    output_dir = Path("knowledge/notion")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{page_id}.md"
    output_path.write_text("\n\n".join(lines), encoding="utf-8")

    print(f"Exported: {output_path}")


if __name__ == "__main__":
    main()
