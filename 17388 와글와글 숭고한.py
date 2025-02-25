# 세 대학의 참여도를 공백으로 구분하여 정수로 입력받음
S, K, H = map(int, input().split())

# 전체 참여도의 합을 계산함
total = S + K + H

# 전체 참여도가 100 이상이면 "OK"를 출력
if total >= 100:
    print("OK")
else:
    # 참여도가 가장 낮은 대학을 찾아 해당 대학의 영문 이름을 출력
    min_val = min(S, K, H)
    if min_val == S:
        print("Soongsil")
    elif min_val == K:
        print("Korea")
    else:
        print("Hanyang")
