n = int(input())

if n == 1:
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, no more bottles of beer on the wall.")
    print()
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 1 bottle of beer on the wall.")
elif n >= 2:
    for i in range(n, 0, -1):
        if i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
        elif i == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.")
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        print()
    
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print(f"Go to the store and buy some more, {n} bottles of beer on the wall.")
