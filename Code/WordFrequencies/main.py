# Write a program that can print out the frequency of each word in a text file.

import fileinput
import collections
import re

freq = collections.Counter()

def clean(token):
    token = token.lower()
    match = re.findall(r'\w+', token)        
    if len(match) > 0:
        return match[0]
    
for line in fileinput.input():
    tokens = line.split()
    for t in tokens:
        t = clean(t)
        if not t:
            continue
        freq[t] += 1

for word, f in freq.most_common():
    if f < 5:
        continue
    print("{: 8d}\t{}".format(f, word))

print(f"estimated vocabulary size: {len(freq)}")
