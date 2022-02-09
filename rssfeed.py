import feedparser
import opml

outline = opml.parse("feedly-7afe47d6-236f-442b-a87c-1e8e7c31ac59-2022-02-09.opml")

for category in outline:
    print(category.title)

    for site in category:
        print(" " + site.title)

        feedUrl = site.xmlUrl
        rssFeed = feedparser.parse(feedUrl)

        for entry in rssFeed.entries:
            print("  " + entry.title)


