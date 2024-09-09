n, m =map(int,input().split())

inter_count=0

nset=set()
mset=set()


for _ in range(n):
    nset.add(input())
    
for _ in range(m):
    mset.add(input())

intersect=mset.intersection(nset)

print(len(intersect))
for name in sorted(intersect):
    print(name)



# interset=nset.intersection(mset)
# inter_count += len(interset)
# print(interset, inter_count)
#         # if n.intersection(m):

#         #     inter_count+=1

#         #     print(inter_count, n.intersection(m)) 