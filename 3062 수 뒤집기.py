import sys
input = sys.stdin.readline

def reverse_num(n):
    return int(str(n)[::-1])

def palindrome(n):
    return str(n) == str(n)[::-1]

T = int(input())

for _ in range(T):
    N = int(input())
    reversed_N = reverse_num(N)
    sum_N = N + reversed_N
    
    if palindrome(sum_N):
        print("YES")
    else:
        print("NO")
