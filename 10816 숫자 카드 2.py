from collections import Counter


N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
query_numbers = list(map(int, input().split()))

card_counter = Counter(numbers)

result = [card_counter.get(q, 0) for q in query_numbers]

print(' '.join(map(str, result)))