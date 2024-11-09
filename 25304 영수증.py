budget = int(input())
count = int(input())
result = 0
for _ in range(count):
    cost, items = map(int, input().split())
    itemcost = cost * items
    result += itemcost  

if result == budget:  
    print("Yes")
else:
    print("No")