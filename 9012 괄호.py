t = int(input())

for _ in range(t):
    ps = input().strip()
    stack = []
    vps= True

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                vps = False
                break
            stack.pop()
    
    if stack:
        vps = False
    
    print("YES" if vps else "NO")