import sys
input = sys.stdin.readline

n, k = map(int,input().split())
ppl = list(range(1,n+1))
result = []
index = 0

while ppl:
    index = (index+k-1)%len(ppl)
    result.append(ppl.pop(index))

print("<" + ", ".join(map(str, result)) + ">")


