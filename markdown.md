---
title: Create your site with Markdown and pandoc.
date: 2025-09-13
---
# In 2025, you can write your page in MARKDOWN and convert it to HTML
Yes!, as you heard.

### Just using the following command**

```bash
pandoc -s index.md -o index.html
```
Or you can use `cmark` also.

---

### Build your site ONLINE now.

# RSS support

```bash
pandoc -t rss --template=feed.xml.template --output=feed.xml --variable=site_url=https://example.com your_markdown_file.md
```
You'll also need a `feed.xml.template` file containing:

```bash
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>$title$</title>
    <link>$site_url$</link>
    <description>$description$</description>
    <language>en-us</language>
    <lastBuildDate>$date$</lastBuildDate>
    <item>
      <title>$title$</title>
      <link>$site_url$/path/to/post</link>
      <description>$body$</description>
      <pubDate>$date$</pubDate>
    </item>
  </channel>
</rss>

```

---

Copyleft 2025
