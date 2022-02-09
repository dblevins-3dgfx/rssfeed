import feedparser
import opml

url = "http://news.ycombinator.com/rss"

outline = opml.parse("feedly-7afe47d6-236f-442b-a87c-1e8e7c31ac59-2022-02-09.opml")

print(outline[0].title)
print(outline[0][0].title)

url = outline[0][0].xmlUrl
d = feedparser.parse(url)

for entry in d.entries:
    print(entry.title)


