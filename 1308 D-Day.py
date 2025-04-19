def main():
    import sys
    input = sys.stdin.read().split()
    sy, sm, sd = map(int, input[:3])
    ey, em, ed = map(int, input[3:])

    # Check for gg condition
    target_y = sy + 1000
    target_m = sm
    target_d = sd
    gg = False
    if ey > target_y:
        gg = True
    elif ey == target_y:
        if em > target_m:
            gg = True
        elif em == target_m and ed >= target_d:
            gg = True
    
    if gg:
        print("gg")
        return

    # Helper functions
    def is_leap(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    def days_in_month(m, y):
        if m == 2:
            return 29 if is_leap(y) else 28
        elif m in [4,6,9,11]:
            return 30
        else:
            return 31

    def compute_days(y, m, d):
        years = y - 1
        leap_days = years // 4 - years // 100 + years // 400
        total = years * 365 + leap_days
        for month in range(1, m):
            total += days_in_month(month, y)
        total += d
        return total

    start = compute_days(sy, sm, sd)
    end = compute_days(ey, em, ed)
    print(f"D-{end - start}")

if __name__ == "__main__":
    main()
