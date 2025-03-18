import sys
input = sys.stdin.readline

def dfs(depth):
    if len(depth) == M:
        print(" ".join(map(str, depth)))
        return
    for i in range(1, N + 1):
        depth.append(i)
        dfs(depth)
        depth.pop()

N, M = map(int, input().split())
dfs([])
