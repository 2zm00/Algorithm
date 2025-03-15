from collections import Counter

word = input().upper()
count = Counter(word)
most_common = count.most_common(2)

if len(most_common) == 1:
    print(most_common[0][0])
else:
    a, b = most_common
    print('?' if a[1] == b[1] else a[0])
