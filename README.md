# rpi-notion
Raspberry Pi Control Hub

HOW TO RUN

`build` docker build -t rpi-notion .

`run` docker run --privileged -t rpi-notion

Need Environment Variables
NOTION_CLIENT_KEY=${get from notion developer}
NOTION_DATABASE_ID=${what table do you want to add to from notion}
