import sys


while True: 
    try:
        a = sys.stdin.readline().strip()
        print(a)
    except EOFError:
        break
