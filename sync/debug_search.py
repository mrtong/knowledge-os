from sync.notion_client import NotionClient

client = NotionClient()

results = client.search()

print(f"Found {len(results)} objects")

for item in results:
    object_type = item.get("object")
    object_id = item.get("id")

    title = "Untitled"

    if object_type == "page":
        for prop in item.get("properties", {}).values():
            if prop.get("type") == "title":
                title_parts = prop.get("title", [])
                title = "".join(t.get("plain_text", "") for t in title_parts) or "Untitled"

    elif object_type == "database":
        title_parts = item.get("title", [])
        title = "".join(t.get("plain_text", "") for t in title_parts) or "Untitled Database"

    print(f"{object_type}: {title} ({object_id})")
