import random

rsp = ['가위','바위','보']
computer_pick = random.choice(rsp)
player_pick = input('가위, 바위, 보 중 하나를 선택하세요. ')

if computer_pick == player_pick :
    print('비겼습니다.')
elif (computer_pick == '가위' and player_pick == '바위') or (computer_pick == '바위' and player_pick == '보') or (computer_pick == '보' and player_pick == '가위'):
    print('YOU WIN')
else:
    print('YOU LOSE')