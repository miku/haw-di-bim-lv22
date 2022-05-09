import xml.etree.ElementTree as ET
from jinja2 import Template

# Parse data
tree = ET.parse('index-rss.xml')
root = tree.getroot()

# Prepare target
docs = []

# Iterate over items
for item in root.iter('{http://purl.org/rss/1.0/}item'):
    doc = {
        "title": item.find('{http://purl.org/rss/1.0/}title').text,
        "link": item.find('{http://purl.org/rss/1.0/}link').text,
        "description": item.find('{http://purl.org/rss/1.0/}description').text,
        "date": item.find('{http://purl.org/dc/elements/1.1/}date').text,
    }
    docs.append(doc)

# Write out a rendered template.
with open("template.html", "r") as f:
    t = Template(f.read())
    print(t.render(docs=docs))
