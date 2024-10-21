#첫재쭐 N, M 공백으로
# N = 100원 // M원
# 초코바 살 수 있으면 yes no

n ,m = map(int,input().split())

if n*100>= m:
	print("Yes")
else:
	print("No")