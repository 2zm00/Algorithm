

while True:
    a, b, c = map(int,input().split())
    
    if a==0 and b==0 and c==0:
        break
    if a>b and a>c:
        if a**2 == b**2 + c**2:
            print("right")
        else:
            print("wrong")
    if b>a and b>c:
        if b**2 == a**2 + c**2:
            print("right")
        else:
            print("wrong")
    if c>b and c>a:
        if c**2 == b**2 + a**2:
            print("right")
        else:
            print("wrong")
    