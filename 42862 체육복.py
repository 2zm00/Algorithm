def solution(n, lost, reserve):
    lost_set=set(lost)
    reserve_set=set(reserve)
    
    common = lost_set & reserve_set
    lost_set -= common
    reserve_set -= common
    
    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    
    answer = n-len(lost_set)
    

    return answer






####### 문제 설명
# 체격 순으로 매겨져있음
# 바로 앞 또는 뒤 에게만 빌려줄 수 잇음

# 전체 학생 N, 도난자 lost, 여벌 reserve
# 최댓값을 리턴하는 솔루션 함수작성

####### 제약조건
# 전체학생수는 2<=n<=30
# lost는 1<=lost<=n // 중복없음
# reserve는 1<=reserve<=n // 중복없음
# reserve만 빌려줄 수 있음
# reserve도 lost가 될 수 있음. 하나만 도난당했다고 가정 -> 이러면 빌려줄 수 없음