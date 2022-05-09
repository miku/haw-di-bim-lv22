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

total, estimated_vocabulary_size = 0, 0
for word, freq in freq.most_common():
    if freq < 5:
        continue
    total += freq
    estimated_vocabulary_size += 1
    print("{: 8d}\t{}".format(freq, word))

print(f"total words: {total} and estimated vocabulary size: {estimated_vocabulary_size}")
