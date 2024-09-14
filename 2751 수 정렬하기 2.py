import sys

n = int(sys.stdin.readline())
#숫자의 갯수 입력 받기

li=[]
#오름차순으로 받을 숫자의 리스트 생성
for _ in range(n):
#n의 갯수까지 반복문
    li_input=int(sys.stdin.readline())
    #두번째줄부터 입력받을 수 입력
    li.append(li_input)
    #리스트에 추가

li.sort()
#리스트 정렬
for i in li:
    print(i)
        #오름차순 순서대로 출력