#1부터 n까지 합을 출력한다. #https://www.acmicpc.net/problem/8393 

N = int(input())

total = 0
for i in range(1,N+1):
    total += i
print(total)