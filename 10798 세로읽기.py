read_longitude = [input() for _ in range(5)]
for i in range(15):
    for j in range(15):
        try:
            print(read_longitude[j][i], end=' ')
        except:
            pass