T = int(input())

for _ in range(T):
    ps = input().strip()
    stack = []
    is_valid = True
    
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                is_valid = False
                break
            stack.pop()
    
    if stack:
        is_valid = False
    
    print("YES" if is_valid else "NO")