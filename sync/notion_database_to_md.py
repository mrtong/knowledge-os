from sync.notion_client import NotionClient
from sync.markdown_writer import MarkdownWriter
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

client = NotionClient()
writer = MarkdownWriter()

pages = client.query_database(DATABASE_ID)

print(f"Found {len(pages)} pages")

for page in pages:

    title = "Untitled"

    for prop in page["properties"].values():

        if prop["type"] == "title":

            title_array = prop["title"]

            if title_array:
                title = "".join(
                    t["plain_text"]
                    for t in title_array
                )

    print(title)
