
freq = {}

with open("61753-0.txt") as f:
    for line in f:
        tokens = line.split()
        for token in tokens:
            if token in freq:
                freq[token] += 1
            else:
                freq[token] = 1

for word, f in freq.items():
    print("{}\t{}".format(f, word))
    
# 2       bestand,
# 1       hart
# 1       zusetzen
# 1       eröffnete
# 2       Verhandlung
# 1       fortzusetzen
# 1       mildernden
# 1       kommen:
# 1       Unglücks
# 1       Innendepartement)
# 1       Ehefrau
# 1       gründet
# 1       (als
# 1       häßlichsten
# 1       woraus
# 3       Dinge,
# 1       Rache
# 6       Revanche
# 1       hervorruft.
