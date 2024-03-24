H, M = map(int,input().split())

#24시간 표현에서 45분 이전으로 알람설정 하기 (H:Hour, M:Minute)

if M < 45 :
    if H==0 :
        H=23
        M+=60
    else :
        H-=1
        M+=60

print (H, M-45)
