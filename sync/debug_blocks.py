from sync.notion_client import NotionClient


def get_title(item):
    if item.get("object") == "database":
        title_parts = item.get("title", [])
        return "".join(t.get("plain_text", "") for t in title_parts) or "Untitled Database"

    for prop in item.get("properties", {}).values():
        if prop.get("type") == "title":
            return "".join(t.get("plain_text", "") for t in prop.get("title", [])) or "Untitled"

    return "Untitled"


def block_text(block):
    block_type = block.get("type")
    content = block.get(block_type, {})

    if "rich_text" not in content:
        return ""

    return "".join(t.get("plain_text", "") for t in content["rich_text"])


client = NotionClient()
results = client.search()

for item in results:
    if item.get("object") != "page":
        continue

    title = get_title(item)
    page_id = item["id"]

    blocks = client.get_block_children(page_id)

    if not blocks:
        print(f"EMPTY: {title}")
        continue

    print(f"\nFOUND PAGE WITH CONTENT: {title}")
    print(f"PAGE ID: {page_id}")
    print(f"BLOCKS: {len(blocks)}\n")

    for block in blocks:
        print(f"- {block.get('type')}: {block_text(block)[:120]}")

    break