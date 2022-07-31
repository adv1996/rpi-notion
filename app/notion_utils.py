import os
from notion_client import Client

NOTION_CLIENT_KEY = os.environ.get("NOTION_CLIENT_KEY")

client = Client(auth=NOTION_CLIENT_KEY)

def createDatabaseRecord(database_id, property, content):
  page = {
    property: [
      {
        "text": {
          "content": content
        }
      }
    ]
  }
  try:
    results = client.pages.create(parent={"database_id": database_id}, properties=page)
    return results['id']
  except Exception as e:
    print(e)
    return False

def addPageBlocks(blockId, children):
  try:
    results = client.blocks.children.append(block_id=blockId, children=children)
  except Exception as e:
    print(e)
