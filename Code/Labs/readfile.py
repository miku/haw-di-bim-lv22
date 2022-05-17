import json

with open("DE-18-285.json") as f:
    doc = json.load(f)
    for k, v in doc.items():
        print(k, v)
