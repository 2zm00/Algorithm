def get_sum_counts(a1, b1, a2, b2):
    min_sum = a1 + a2
    max_sum = b1 + b2
    counts = [0] * (max_sum - min_sum + 1)
    for x in range(a1, b1 + 1):
        for y in range(a2, b2 + 1):
            s = x + y
            counts[s - min_sum] += 1
    return counts, min_sum, max_sum

# 입력 처리
g_a1, g_b1, g_a2, g_b2 = map(int, input().split())
e_a1, e_b1, e_a2, e_b2 = map(int, input().split())

# 각각의 합 분포 계산
g_counts, g_min, g_max = get_sum_counts(g_a1, g_b1, g_a2, g_b2)
e_counts, e_min, e_max = get_sum_counts(e_a1, e_b1, e_a2, e_b2)

# 석의 누적합 계산
e_size = e_max - e_min + 1
cum_e = [0] * (e_size + 1)
current = 0
for i in range(e_size):
    current += e_counts[i]
    cum_e[i + 1] = current

total_e = current

win_g, tie, win_e = 0, 0, 0

# 꿍의 각 합 처리
for s_g in range(g_min, g_max + 1):
    idx_g = s_g - g_min
    cnt_g = g_counts[idx_g]
    if cnt_g == 0:
        continue
    
    s_e_less = s_g - 1
    if s_e_less < e_min:
        count_less = 0
    elif s_e_less > e_max:
        count_less = total_e
    else:
        idx_e = s_e_less - e_min
        if idx_e >= len(cum_e) - 1:
            count_less = total_e
        else:
            count_less = cum_e[idx_e + 1]
    
    if e_min <= s_g <= e_max:
        count_eq = e_counts[s_g - e_min]
    else:
        count_eq = 0
    
    count_more = total_e - count_less - count_eq
    
    win_g += cnt_g * count_less
    tie += cnt_g * count_eq
    win_e += cnt_g * count_more

if win_g > win_e:
    print("Gunnar")
elif win_g < win_e:
    print("Emma")
else:
    print("Tie")
