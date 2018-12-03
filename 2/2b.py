import sys

words = []

for l in sys.stdin:
    words.append(l.strip())

seen = [set() for _ in range(len(words[0]))]

for word in words:
    for j in range(len(word)):
        sub_word = word[:j] + word[j + 1:]
        if sub_word in seen[j]:
            print(sub_word)
        seen[j].add(sub_word)
