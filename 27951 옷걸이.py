import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
u, d = map(int, sys.stdin.readline().split())

type1 = type2 = type3 = 0
for num in a:
    if num == 1:
        type1 += 1
    elif num == 2:
        type2 += 1
    else:
        type3 += 1

use_u_type1 = min(type1, u)
u_remaining = u - use_u_type1
use_d_type2 = min(type2, d)
d_remaining = d - use_d_type2

if u_remaining + d_remaining > type3:
    print("NO")
else:
    res = []
    u_r, d_r = u_remaining, d_remaining
    for num in a:
        if num == 1:
            res.append('U')
        elif num == 2:
            res.append('D')
        else:
            if u_r > 0:
                res.append('U')
                u_r -= 1
            else:
                res.append('D')
                d_r -= 1
    print("YES")
    print(''.join(res))
