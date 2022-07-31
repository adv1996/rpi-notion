
def createRichText(content):
  return {
    "rich_text": [
      {
        "text": {
          "content": content
        }
      }
    ]
  }

def createBlockDivider(text_type, content):
  return {
    text_type: {}
  }

def createTextBlock(text_type, content):
  return {
    text_type: createRichText(content)
  }

blockMap = {
  'divider': createBlockDivider,
  'paragraph': createTextBlock,
  'heading_3': createTextBlock,
  'bulleted_list_item': createTextBlock,
  'to_do': createTextBlock
}

def createBlock(type, content):
  if type in blockMap:
    return blockMap[type](type, content)
  else:
    return blockMap['divider'](type, content)

def blockBuilder(blocks):
  return list(map(lambda block: createBlock(block['type'], block['content']), blocks))