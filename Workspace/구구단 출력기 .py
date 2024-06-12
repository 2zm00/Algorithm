print("알고싶은 구구단은 무엇인가요?")

user_choice = int(input())

if user_choice>=10:
    for i in range (1,user_choice+1):
        print(user_choice, 'x', i, '=', user_choice*i)
else:
    for i in range (1,10):
        print(user_choice, 'x', i, '=', user_choice*i)




