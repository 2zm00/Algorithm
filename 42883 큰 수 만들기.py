def solution(number, k):
    num_list = []
    number_str = str(number)
    
    for digit_str in number_str:
        digit = int(digit_str)
        
        # 현재 숫자보다 작은 이전 숫자 제거 (k 감소)
        while num_list and k > 0 and num_list[-1] < digit:
            num_list.pop()
            k -= 1
        
        # 현재 숫자 추가 (무조건 수행)
        num_list.append(digit)
    
    # 남은 k 처리: 뒤에서 k개 제거
    if k > 0:
        num_list = num_list[:-k]
    
    
    
    
    answer = str(''.join(map(str, num_list)))
    # 마지막에 형식이 숫자가 아니라 문자열 형태로 요구해서 str로 일단 수정
    
    return answer


####### 제약 조건
# len(number) >= 2
# 1 <= k <= len(number) / 자연수

####### 풀이
# number에서 각 자릿수 숫자를 뽑아
# 정렬한 것 중에서 작은 것부터 k 만큼 제거
# number를 숫자로 변환

# 각 자릿수 숫자 뽑기
# 숫자를 문자열로 변환
# for 문으로 문자열로 변한 숫자를 순회해서 정수로 전환해서 빈 리스트에 넣기

# 생각을 잘못했음..
# 다시 생각해서 보면 4177252841에서 자릿수로 쪼개진 상태에서 봐야함
# 앞 뒤 숫자가 자기보다 작으면 삭제해야함
# 4>1<7=7>2<5>2<8>4<1 이므로
# k=1 일 때 4<7=7>2<5>2<8>4>1
# k=2 일 때 7=7>2<5>2<8>4>1
# k=3 일 때 7=7>5>2<8>4>1
# k=4 일 때 7=7>5<8>4>1 이므로 답은 775841이 나오는 것

# 그러기 위해선 뭘 해야하냐..
# 하나씩 리스트로 들어갈때
# 리스트 안에 숫자와 비교해서 작으면 삭제함
# 그리고 k를 하나 줄임
# k가 0이 되면 종료
# k가 0이 되지 않으면 리스트에 숫자를 넣음