import sys

a, b = map(int, sys.stdin.readline().split())

# 최대공약수 구하기 (유클리드 알고리즘)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최소공배수 구하기
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

