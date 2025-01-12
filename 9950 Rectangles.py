def solve_rectangles(input_lines):
    results = []
    for line in input_lines:
        l, w, a = map(int, line.split())
        if l == 0 and w != 0:  # 길이가 없는 경우
            l = a // w
        elif w == 0 and l != 0:  # 너비가 없는 경우
            w = a // l
        elif a == 0 and l != 0 and w != 0:  # 면적이 없는 경우
            a = l * w
        results.append(f"{l} {w} {a}")
    return results

# 입력 처리
while True:
    line = input()
    if line == "0 0 0":  # 종료 조건
        break
    l, w, a = map(int, line.split())
    if l == 0 and w != 0:
        l = a // w
    elif w == 0 and l != 0:
        w = a // l
    elif a == 0 and l != 0 and w != 0:
        a = l * w
    print(f"{l} {w} {a}")
