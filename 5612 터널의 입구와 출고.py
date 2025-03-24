n = int(input())
m = int(input())
max_cars = m

for i in range(n):
    enter, exit = map(int, input().split())
    m = m + enter - exit
    if m < 0:
        max_cars = 0
        break
    if m > max_cars:
        max_cars = m

print(max_cars)
