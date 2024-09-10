n, m, k = map(int,input().split())

# n = 카드의 갯수
# m = 앞면에 O가 적힌 카드
# k = 뒷면에 O그릴 카드 갯수
plus = 0

frontx=n-m
backx=n-k

if frontx<=backx:
    plus+=frontx
else :
    plus+=backx

if m<=k:
    plus+=m
else:
    plus+=k

print(plus)
print("총 카드",n,"앞d",m,"앞x",frontx,"뒷d",k,"뒷x",backx)


