from sync.notion_client import NotionClient


def get_title(item):
    for prop in item.get("properties", {}).values():
        if prop.get("type") == "title":
            return "".join(t.get("plain_text", "") for t in prop.get("title", [])) or "Untitled"
    return "Untitled"


client = NotionClient()
results = client.search()

for item in results:
    if item.get("object") != "page":
        continue

    title = get_title(item)
    print(f"{title} | {item['id']}")
