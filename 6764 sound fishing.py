# 4개의 수심 측정값을 입력받습니다
depths = []
for _ in range(4):
    depth = int(input())
    depths.append(depth)

# 수심 패턴을 확인합니다
if depths[0] < depths[1] < depths[2] < depths[3]:
    print("Fish Rising")
elif depths[0] > depths[1] > depths[2] > depths[3]:
    print("Fish Diving")
elif depths[0] == depths[1] == depths[2] == depths[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")
