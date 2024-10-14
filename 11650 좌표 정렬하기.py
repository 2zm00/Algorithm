# x좌표가 증가하는 순 으로
# x좌표가 같으면 y좌표가 증가하는 순서로 정렬


#갯수 입력받기
#점들을 (x,y)로 한세트로 묶기
#먼저 x정렬하기, x가 같다면 y로 정렬하기

n = int(input())
dots = []

for _ in range(n):
	x,y = map(int,input().split())
	dots.append((x,y))

sorted_dots = sorted(dots, key=lambda dot: (dot[0], dot[1]))

for dot in sorted_dots:
    print(dot[0], dot[1])
