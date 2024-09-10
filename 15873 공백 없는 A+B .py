n = int(input())
a=0 
b=0
if n%10==0:
    b=10
    a=n//100
else:
    a=n//10
    b=n%10

print(a+b)