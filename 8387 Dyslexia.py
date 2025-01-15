# 입력 받기
n = int(input())  # 텍스트 길이
original_text = input()  # 원본 텍스트
rewritten_text = input()  # 다시 작성된 텍스트

# 올바르게 재작성된 문자 수 계산
correct_count = sum(1 for o, r in zip(original_text, rewritten_text) if o == r)

# 결과 출력
print(correct_count)
