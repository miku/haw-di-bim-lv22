
import json

with open("export.json") as f:
    doc = json.load(f)

# (1) count incoming
# (2) count outgoing

out = 0
in_ = 0

for item in doc["data"]["bibliothek_ausleihe_ausgang-eingang"]:
    if item["outgoing"]:
        out += 1
    if item["incoming"]:
        in_ += 1

print(out)
print(in_)
