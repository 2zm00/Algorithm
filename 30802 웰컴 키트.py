n = int(input())
size = map(int,input().split())
t, p = map(int,input().split())

bd = 0

for sz in size:
    if sz == 0 :
        continue
    elif sz < t :
        bd += 1
    elif sz >= t :
        bd += sz//t
        if sz%t > 0:
            bd += 1



print(bd)
print(n//p, n%p)

