import sys

n = int(sys.stdin.readline())
members = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), i, name))

members.sort(key=lambda x: (x[0], x[1]))

for age, _, name in members:
    print(f"{age} {name}")
