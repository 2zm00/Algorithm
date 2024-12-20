def count_ways(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        # N층에서의 경우의 수는 2^n
        return 2 ** n

# 입력 받기
N = int(input())
# 결과 출력
print(count_ways(N))
