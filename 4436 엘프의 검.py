def check_all_digits(num_str):
    # 0부터 9까지 모든 숫자가 있는지 확인
    return all(str(digit) in num_str for digit in range(10))

def find_k(n):
    k = 1
    digits = ''
    
    # k를 1씩 증가시키면서 확인
    while True:
        # 현재 k에 대한 n*k 계산
        current = str(n * k)
        # 이전에 나온 숫자들과 합침
        digits = digits + current
        
        # 모든 숫자가 있는지 확인
        if check_all_digits(digits):
            return k
        k += 1

# 입력 처리
while True:
    try:
        n = int(input())
        print(find_k(n))
    except:
        break
