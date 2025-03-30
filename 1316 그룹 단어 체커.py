def is_group_word(word):
    """주어진 단어가 그룹 단어인지 판별하는 함수."""
    seen = set()
    prev = ''
    for char in word:
        if char in seen and char != prev:
            return False
        seen.add(char)
        prev = char
    return True

def solve():
    """그룹 단어 체커 문제 해결 함수."""
    n = int(input())
    words = [input() for _ in range(n)]
    
    count = 0
    for word in words:
        if is_group_word(word):
            count += 1
    
    print(count)

solve()
