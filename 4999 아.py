# 두 줄의 입력을 받습니다
jaehwan = input()  # 재환이가 낼 수 있는 "aah"
doctor = input()   # 의사가 원하는 "aah"

# 재환이가 낼 수 있는 소리의 길이가 의사가 원하는 길이보다 크거나 같으면 "go" 출력
print("go" if len(jaehwan) >= len(doctor) else "no")