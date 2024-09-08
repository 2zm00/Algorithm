n = int(input())
scores = list(map(int,input().split()))
newtotal = 0


maximum = max(scores)

for score in scores:
    new = score/maximum*100
    newtotal += new

print(new)
print(maximum)
print(newtotal/n)