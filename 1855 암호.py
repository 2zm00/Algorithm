def decrypt_message(K, encrypted_string):
    # 행의 개수 계산
    rows = len(encrypted_string) // K
    
    # 빈 그리드 생성
    grid = [['' for _ in range(K)] for _ in range(rows)]
    
    # 지그재그 패턴으로 그리드 채우기
    current_index = 0
    direction = 1  # 1: 왼쪽->오른쪽, -1: 오른쪽->왼쪽
    
    for row in range(rows):
        if direction == 1:
            # 왼쪽에서 오른쪽으로
            for col in range(K):
                grid[row][col] = encrypted_string[current_index]
                current_index += 1
            direction = -1
        else:
            # 오른쪽에서 왼쪽으로
            for col in range(K-1, -1, -1):
                grid[row][col] = encrypted_string[current_index]
                current_index += 1
            direction = 1
    
    # 열별로 문자열 재구성
    original_string = ''
    for col in range(K):
        for row in range(rows):
            original_string += grid[row][col]
    
    return original_string

# 입력 받기
K = int(input())
encrypted_string = input()

# 결과 출력
result = decrypt_message(K, encrypted_string)
print(result)
