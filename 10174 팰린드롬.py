n = int(input())
for _ in range(n):
    s = input().strip()
    s_lower = s.lower()
    print("Yes" if s_lower == s_lower[::-1] else "No")
