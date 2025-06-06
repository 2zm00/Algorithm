from collections import deque

MAX = 100001
n, k = map(int, input().split())
dist = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < MAX and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs()
