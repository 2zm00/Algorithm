#각 테스트 케이스마다 A+B를 출력한다.

while True:
    try :
        A, B=map(int,input().split())
        print (A+B)
    except : 
        break