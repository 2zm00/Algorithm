a_time, a_dmg = map(int,input().split())
b_time, b_dmg = map(int,input().split())
c_time, c_dmg = map(int,input().split())
hp = int(input())
time = 0

# 0초에 모든 마스코트가 동시에 공격
hp -= (a_dmg + b_dmg + c_dmg)

# 초기 공격으로 핑크빈이 쓰러지지 않은 경우
if hp > 0:
    # 핑크빈의 체력이 0 이하가 될 때까지 반복
    while True:
        time += 1
        damage = 0
        
        # 각 마스코트의 스킬 주기를 체크하여 데미지 계산
        if time % a_time == 0:
            damage += a_dmg
        if time % b_time == 0:
            damage += b_dmg
        if time % c_time == 0:
            damage += c_dmg
            
        hp -= damage
        
        # 핑크빈의 체력이 0 이하가 되면 종료
        if hp <= 0:
            break

print(time)