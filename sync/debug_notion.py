import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("NOTION_TOKEN")
PAGE_ID = os.getenv("NOTION_PAGE_ID")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Notion-Version": "2022-06-28",
}

url = f"https://api.notion.com/v1/pages/{PAGE_ID}"

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text)
