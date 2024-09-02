import math

a = list(map(int,input().split()))

apow = sum(x ** 2 for x in a)
print (apow%10)