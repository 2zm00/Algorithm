def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i ==0:
            return False
        return True


n=int(input())
a= list(map(int,input().split()))
b=0


for num in a:
    if prime(num):
        b+=1

print(b)