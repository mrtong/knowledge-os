import os
from urllib import response
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_VERSION = "2022-06-28"


class NotionClient:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {NOTION_TOKEN}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def search(self):
        url = "https://api.notion.com/v1/search"

        response = requests.post(
            url,
            headers=self.headers,
            json={
                "page_size": 20
            },
        )

        response.raise_for_status()
        return response.json()["results"]

    def get_page(self, page_id):
        url = f"https://api.notion.com/v1/pages/{page_id}"

        response = requests.get(
            url,
            headers=self.headers,
        )

        response.raise_for_status()
        return response.json()


    def get_block_children(self, block_id):
        url = f"https://api.notion.com/v1/blocks/{block_id}/children"

        response = requests.get(
            url,
            headers=self.headers,
            params={"page_size": 100},
        )

        response.raise_for_status()
        return response.json()["results"]

    def query_database(self, database_id):
        url = f"https://api.notion.com/v1/databases/{database_id}/query"

        response = requests.post(
            url,
            headers=self.headers,
            json={},
        )

        response.raise_for_status()
        return response.json()["results"]
