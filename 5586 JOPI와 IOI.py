def count_joi_ioi(s):
    joi_count = 0
    ioi_count = 0
    
    # 문자열을 순회하면서 3글자씩 확인
    for i in range(len(s) - 2):
        if s[i:i+3] == 'JOI':
            joi_count += 1
        elif s[i:i+3] == 'IOI':
            ioi_count += 1
    
    return joi_count, ioi_count

# 입력 받기
s = input()

# 결과 계산
joi, ioi = count_joi_ioi(s)

# 결과 출력
print(joi)
print(ioi)
