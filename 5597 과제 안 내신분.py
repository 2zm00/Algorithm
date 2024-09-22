allstd = set(range(1,31))
attd = set()

for _ in range(28):
    attd.add(int(input()))

notattd = allstd - attd

print(min(notattd))
print(max(notattd))