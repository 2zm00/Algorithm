month = int(input())
day = int(input())

# 조건에 따라 결과 출력
if month < 2:
    print("Before")
elif month > 2:
    print("After")
else:  # month == 2인 경우
    if day < 18:
        print("Before")
    elif day > 18:
        print("After")
    else:  # day == 18인 경우
        print("Special")