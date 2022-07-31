from gpiozero import Button
from signal import pause
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")

from notion_utils import createDatabaseRecord, addPageBlocks
from block_builder import blockBuilder
import datetime
import pytz

timeZ_Ny = pytz.timezone('America/New_York')

def driver():
  print('CREATING NOTION RECORD')
  start_time = datetime.datetime.now(timeZ_Ny)
  current_time = start_time.strftime("%I:%M %p")
  time_change = datetime.timedelta(hours=8)
  end_time = (start_time + time_change).strftime("%I:%M %p")
  todays_date = start_time.strftime('%m/%d/%Y')

  pageId = createDatabaseRecord(NOTION_DATABASE_ID, 'Daily Entry', todays_date)

  # TODO: future read from JSON templates?

  blocks = [
    {
      "type": 'paragraph',
      "content": 'Let\'s get this day started!'
    },
    {
      "type": 'bulleted_list_item',
      "content": f'Start Time - {current_time}'
    },
    {
      "type": 'bulleted_list_item',
      "content": f'End Time - {end_time}'
    },
    {
      "type": 'paragraph',
      "content": ''
    },
    {
      "type": 'heading_3',
      "content": 'Work Life'
    },
    {
      'type': 'divider',
      'content': ''
    },
    {
      "type": "to_do",
      "content": ""
    },
    {
      "type": 'heading_3',
      "content": 'Freelance Hustle'
    },
    {
      'type': 'divider',
      'content': ''
    },
    {
      "type": "to_do",
      "content": ""
    },
    {
      "type": 'heading_3',
      "content": 'Personal Freedom'
    },
    {
      'type': 'divider',
      'content': ''
    },
    {
      "type": "to_do",
      "content": ""
    }
  ]

  children = blockBuilder(blocks)
  if pageId:
    addPageBlocks(pageId, children)
    print('COMPLETED TASK')
  

if __name__ == "__main__":
  print('RPI_NOTION Ready')
  button = Button(2)

  button.when_pressed = driver

  pause()

# HOW TO RUN
# docker build -t rpi_notion .
# docker run --privileged -t rpi_notion