# site = "http://naver.com"
# site2 = site[7:12]
# print(site2[0:3]+str(len(site2))+str(site2.count("e"))+"!")

"""
site = input("Password Generator\n사이트 주소를 입력하세요: ")

if "http://" in site:
    site = site.replace("http://", "")
if "https://" in site:
    site = site.replace("https://", "")
if "www." in site:
    site = site.replace("www.", "")
if ".com" in site:
    site = site[:site.index(".")]

print(site[:3]+str(len(site))+str(site.count("a"))+"!")
"""


# subway = ["hj", "yb", "yj"]

# print(subway.index("hj"))
# subway.append("jm")
# print(subway)

# subway.insert(2, "ms")
# print(subway)

# subway.pop()
# print(subway)

# # subway.clear()
# subway = ["유재석"]
# subway.append("유재석")

# subway.append("유재석")

# subway.append("유재석")
# print(subway.count("유재석"))


# num_list = [5, 4, 3,2,1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()

# mix_list = ["조세호", 20, True]
# num_list.extend(mix_list)
# print(num_list)

# """key, value, item = dict {}"""
# cabinet = {3:"유재석", 100:"강호동"}
# print(cabinet[3])

# print(cabinet.get(5))
"""대괄호로 했을 때에는 없을 땐 오류 후 종료,
get이용 시 없을 떈 None 발생"""

# print(cabinet.get(5, "사용가능"))


# print(3 in cabinet) # True
# print(5 in cabinet) # False


# cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cabinet)
# cabinet["C-20"] = "조세호"
# print(cabinet)


# del cabinet["A-3"]
# print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())
# # print(cabinet.items())
# cabinet.clear()
"""속도가 튜플이 더 빠르다"""

# menu = ("pasta", "cheeze")
# print(menu[0])
""" add x """

# name = "김종국"
# age = 20
# # hobby = "coding"

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

"""set = 중복이 안되고 순서가 없어"""
# my_set = {1, 2, 3, 4, 5, 4}
# # print(my_set)

# java = {"유재석" , "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# # print(java&python)
# # print(java.intersection(python))

# # print(java|python)
# # print(java.union(python))

# # print(java-python)
# # print(java.difference(python))

# python.add("김태호")
# print(python)
# java.remove("김태호")
# print(java)


"""자료구조의 변경"""

# menu = {"coffee", "juice", "milk"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))
# print(menu)

"""퀴즈4"""
# from random import *
# lst = range(1, 21)
# lst = list(lst)

# # print(lst)
# shuffle(lst)
# # print(lst)
# winner = sample(lst, 4)
# print(winner)
# print(" - - 축하합니다 - - ")
# print("치킨 당첨자 : " + str(winner[0]))
# print("커피 당첨자 : " + str(winner[1:]))
# print(" - - 당첨자 발표 - -")

"""if"""

# weather = input("오늘 날씨는 어떄요? 비/ 미세먼지/ 기타")
# if weather == "비" or weather=="snow":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

"""반복문 for while"""

# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))


# starbucks = ["ironman", "thor", "groot"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

"""while"""

# customer = "thor"
# index = 5
# while index >= 1:
#     print("{0}님, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었숩니다")


# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.".format(customer, index))
#     index += 1

# customer = "thor"
# person = "Unkown"

# while person != customer :
#     print("{0},커피가 준비 됨요.".format(customer))
#     person = input("이름이 어떻게 되세요?")


"""continue : 스킵하고 다음꺼 진행해라
break : 바로 종료"""

# absent = [2, 5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("수업 끝내. {0} 교실 ㄱㄱ".format(student))
#         break

#     print("{0}, 책 읽어줘".format(student))


"""한줄 for """

# students = [1,2,3,4,5]
# print(students)
# students =[i+100 for i in students]
# # # print(students)
# students = ["ironman", "thor", "groot"]
# # students = [len(i) for i in students]
# # print(students)

# students = [i.capitalize() for i in students]
# print(students)

"""quiz 5"""
# from random import *

# cnt = 0

# for i in range(1,51):
#     time = randrange(5,51)
#     if 5<=time<=15:
#         print("[0] {0}번째 손님 (소요시간 : {1})".format(i, time))
#         cnt += 1
#     else : 
#         print("[ ]  {0}쨰 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0}분".format(cnt))

"""함수 = 어떠한 역할을 하는 박스"""
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은{0}".format(balance + money))
#     return balance + money

# def withdraw(balance,money):
#     if balance >= money:
#         print("withdraw complete. balance is {0}".format(balance - money))
#         return balance - money
#     else:
#         print("withdraw error. balance is {0}".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)

# # balance = withdraw(balance, 200)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}이며, 잔액은 {1}".format(commission, balance))


"""기본값"""
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용언어: {2}"\
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "java")
"""이러면 튜플로 들어가는건가???"""
# def profile(name="아무개", age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용언어: {2}"\
#           .format(name, age, main_lang))
    
# profile()

"""키워드 함수호출"""
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=24)
# profile(main_lang="java", age="24", name="taeho")

"""가변인자 = *변수"""
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 :{1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 :{1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "C", "C++", "C#","javas")
# profile("김태호", 25, "Kotiln", "Swift",)

"""지역변수, (권장되는 방법은 아님. 파라미터로 던지고 받는거 추천)전역변수 = global def"""
# gun = 10
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총: {0}".format(gun))


"""퀴즈6"""
# 별으의 함수 내에서 계산 * std_weight 
# 소수점 둘째자리

# def std_weight(gender, height):
#     if gender == "male":
#         return (height**2)*22
#     else : 
#         return (height**2)*21
    
# height = 175
# gender = "male"
# weight = round(std_weight(gender, height/100), 2)
# print("height {0}cm, {1} equals {2}kg".format(height, gender, weight))

''' 입력받아서 하고싶은데..???'''


"""표준입출력"""