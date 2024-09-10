import sys

n = int(input())
words = []

for _ in range(n):
    word = input()
    words.append(word)

words.sort(key=lambda x : (len(x), x))

words=list(dict.fromkeys(words))

for word in words:
    print(word)
