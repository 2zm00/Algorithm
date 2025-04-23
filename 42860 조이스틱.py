alphabet_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25 }
    
def change_name_to_num(name):
    result = []
    for i in name:
        num = alphabet_num[i]
        result.append(num)
    return result

def solution(name):
    move_count=0
    name_count=0
    
    name_num = change_name_to_num(name)
    for num in name_num:
        name_count += min(num, 26-num)
# 내가 미처 생각하지 못했던 것 '최솟값'
    
#     이름의 길이 
    n = len(name)
#     최악인 경우 이름의 길이-1 이 좌우 최솟값일 것
    min_move = n-1
    
    
    
# 여기서 좌우 move_count가 연속적인 A가 나오면 최솟값이 달라질 변수가 있으므로, 연속적인 A가 있는지 확인하고 도출해야함
# 그래서 while 문으로 'A'가 연속으로 나올 때까지 옆으로 이동해야하니까 +1을 해야한다. 그리고 길이가 n을 넘지 않아야해
#     이름의 길이만큼
    for i in range(n):
#         다음 알파벳
        next_idx = i+1
#     만약 다음 알파벳이 마지막까지 도달했고, A가 나올 때 까지
        while next_idx < n and name[next_idx]=='A':
#         다음 알파벳으로 간다
            next_idx += 1
#     숫자 카운트가 이름의 길이+알파벳 개수 + 좌우 이동
        move = i + n - next_idx  + min(i, n-next_idx)
#     중에서 최솟값을 가진다
        min_move = min(min_move, move)
    
#    만약 그 카운트가 최악의 시나리오가 아니라면
    if move < min_move:
#         move 로 최솟값으로 지정한다.
        min_move = move
    
    answer = name_count+min_move
    
        
    
    return answer


# 조이스틱으로 이름 완성하기 A에서 시작해서 원하는 알파벳까지 도달해야되는 듯
# 1. 위/아래로 조작하여 원하는 알파벳 도달
# 2. 도달 후 왼쪽으로 이동해서 1번 반복
# 3. 움직임의 최솟값 리턴하기

# 알파벳 지정하기
# 'A'= 0 ~~~ 'Z' = 25
"""
A0
B1
C2
D3
E4
F5
G6
H7
I8
J9
K10
L11
N12
M13
O14
P15
Q16
R17
S18
T19
U20
V21
W22
X23
Y24
Z25
"""
# 옆으로 이동하는 횟수 추가
# move_count += len(name)
# name_count = 21 = J9 A0 N12 
# 이름변환함수를 만들고
# name 인풋 들어오면
# change_name_to_num(name)
# answer = move_count+name_count


####### 제약조건
# name은 대문자 알파벳
# 1 <= name <= 20


