

def solution(people, limit):
    boat_count = 0
    people.sort(reverse=True)
    heavy = 0
    light = len(people)-1
    
    while heavy <= light:
        if people[light] + people[heavy] <= limit:
            light -= 1
        heavy += 1
        boat_count += 1
    
        
    answer = boat_count
    return answer



# 시간 초과가 뜸
# 이유? pop 쓰는것 때문에 시간초과가 뜨는 것 같음
# 포인터를 쓰면 해결이 될 것 같음 
# 풀이시간 30분

"""
def solution(people, limit):
    boat_count = 0
    
    people.sort(reverse=True)

    while people :
        heavy = people.pop(0)
        if people and heavy + people[-1] <= limit:
            people.pop(-1)
        boat_count += 1
        
    answer = boat_count
    return answer
"""


####### 제약조건
# 1 <= len(people) <= 50000
# 40 <= people <= 240
# 40 <= limit <= 240
# max(people) < limit
# 구명보트 한번에 최대 2명
# 모든 사람 구출하기 위해 필요한 구명보트 갯수 최솟값 = solution


# 문제풀이
# boat_count : 구명보트 갯수
# 사람들을 몸무게 순으로 정렬
# 앞뒤에서 하나씩 뽑아서 limit을 넘지 않는다면, boat_count += 1 하고 리스트에서 pop
# limit을 넘는다면 (예: 0번 1번 초과하면 0,2 0,3 .. 해서 limit과 비교)
# boat_count 를 answer로 넘겨서 제출