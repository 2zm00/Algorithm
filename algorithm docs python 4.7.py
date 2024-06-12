'''def fib(n):
    a,b=0,1
    while a<n:
        print(a, end=' ')
        a,b=b,a+b
    print()

input(fib())'''


A, B = 0, 1

B += A+B
while A<n:
    print(A, end=' ')
    A, B += B, A+B
print(B)