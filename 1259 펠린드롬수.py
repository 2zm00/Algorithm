
while True:
    pal = input()
    if pal == "0":
        break

    is_pal = True

    palist=list(pal)
    for i in range(len(palist) // 2):
        if palist[-i-1] != palist[i]:
            is_pal = False
            break
    if is_pal:
        print("yes")
    else:
        print("no")
