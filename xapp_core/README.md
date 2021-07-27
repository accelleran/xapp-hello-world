# THIS IS AN EXAMPLE PROVIDED README

This document can be used to provide nice and fancy documentation for an xApp.

## Introduction

This document is a text file formated in Markdown. The Markdown language provided the possibility to create formatted text using a plain-text editor.

By following the specific syntax of Markdown, you'll be able to create summaries, tables, code boxes, check lists, include images and much more.

You can find further information reading the following link:

* [Markdown](https://en.wikipedia.org/wiki/Markdown) - Wikipedia Markdown
* [Markdown Guide](https://www.markdownguide.org/cheat-sheet/) - Markdown cheat-sheet
* [Stackedit](https://stackedit.io/app#) - In-browser Markdown Editor
* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Github guide for mastering markdown

## xApp description

The xApp README file generally contains the following element:
- A description of the xApp and its functionality
- If the xApp is sharing data on the dRAX RIC Databus or not
- If the xApp is sharing data, what is the format of the data
- If the xApp is sharing data, which topic on the dRAX RIC Databus is the data shared on

## xApp Data

### xApp Data Description

This xApp shares two kinds of data:
- Example_1
- Example_2

Example_1 represents...

Example_2 represents...

### xApp Data Topic

This xApp publishes data on the following topics:
- example_topic_1 - The xApp publishes Example_1 data on this topic
- example_topic_2 - The xApp publishes Example_2 data on this topic

### xApp Data Format

Example_1 data has the following format:

```json
{
  "type": "example_1",
  "data_1": "some data 1"
}
```

Example_2 data has the following format:

```json
{
  "type": "example_2",
  "data_2": "some data 2"
}
```

## xApp APIs:

This xApp has the following API endpoints exposed:
- /api/actions
- /api/request

### xApp APIs Description

/api/actions is used for...

/api/request is used for...

### xApp APIs usage

/api/actions has the following methods available:
- GET

/api/request has the following methods available:
- GET
- POST

The POST method expects the following parameters:
- ...
- ...

