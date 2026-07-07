# sync/list_database_pages.py

import os
from dotenv import load_dotenv

from sync.notion_client import NotionClient

load_dotenv()


def get_title(item):
    for prop in item.get("properties", {}).values():
        if prop.get("type") == "title":
            return "".join(t.get("plain_text", "") for t in prop.get("title", [])) or "Untitled"
    return "Untitled"


client = NotionClient()
database_id = os.getenv("NOTION_DATABASE_ID")

pages = client.query_database(database_id)

for page in pages:
    print(f"{get_title(page)} | {page['id']}")
