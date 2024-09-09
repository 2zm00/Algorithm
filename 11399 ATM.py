n = int(input())

tset=list(map(int,input().split()))
# print(sorted(tset)) #1 2 3 3 4
tset=sorted(tset)
#최솟값 뽑아낼 수 있도록 크기 순 정렬 완료
total = 0
tsum2 = 0

for time in tset:
    tsum2+=time
    total+=tsum2

print(total)

#이건 지금 [0]~[끝]까지의 합만 주는데 ..
# print(tsum)