n = int(input())
for _ in range(n):
    sentence = input()
    if not sentence.endswith('.'):
        sentence += '.'
    print(sentence)
