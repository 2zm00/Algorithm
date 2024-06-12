#연산자의 기호는 ＠으로, A＠B = (A+B)×(A-B)으로 정의

def ab(A,B):
    result = (A+B)*(A-B)
    return result

A, B = map(int,input().split())

print (ab(A,B))