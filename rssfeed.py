import feedparser
import opml

def traverse(node, visitor, parent):
    visitor(node, parent)
    for child in node:
        traverse(child, visitor, node)
            
root = opml.parse("feedly-7afe47d6-236f-442b-a87c-1e8e7c31ac59-2022-02-09.opml")

def visit_node(o, p):
    indent = ""
    if (hasattr(o, 'type') and o.type == 'rss'):
        indent = "  "
    print(indent + o.title)

traverse(root, visit_node, None)
