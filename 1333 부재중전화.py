def find_earliest_time(n, l, d):
    bell_time = d
    total_time = n * l + (n-1) * 5  # 전체 앨범 재생 시간
    
    while True:
        # 현재 bell_time이 어느 구간에 있는지 계산
        song_idx = bell_time // (l + 5)  # 몇 번째 노래 구간인지
        position = bell_time % (l + 5)   # 구간 내 위치
        
        # 앨범이 끝난 후라면
        if bell_time >= total_time:
            return bell_time
            
        # 현재 곡이 앨범 내의 곡이고
        if song_idx < n:
            # 공백 구간(l <= position < l+5)에 있다면
            if position >= l:
                return bell_time
                
        bell_time += d

# 입력 받기
n, l, d = map(int, input().split())
print(find_earliest_time(n, l, d))
