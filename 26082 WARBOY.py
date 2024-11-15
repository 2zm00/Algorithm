a,b,c = map(int,input().split())

# 경쟁사 가격 a, 경쟁사 성능 b, warboy 가격 c.
# warboy성능은 3b

pp = b//a
x = 3*pp*c

print(x)