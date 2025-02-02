import math

a, b = map(int, input().split())
print(abs(a * b) // math.gcd(a, b))
