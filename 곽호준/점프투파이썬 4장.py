#4-1
# def is_add(number):
#     if number % 2 == 1:
#         print("홀수")
#     else:
#         print("짝수")

# test_number = 13
# is_add(test_number)

# is_add = lambda number: print("홀수") if number % 2 ==1 else print("짝수")

# test_number = 13
# is_add(test_number)

#4-2
# def get_avg(*list):
#     total = 0
#     for i in list:
#         total = total + i
#     return total / len(list)

# print(get_avg(1,2,3,4,5))

# def get_avg(list):
#     total = 0
#     for i in list:
#         total = total + i
#     return total / len(list)

# test_list = [1,2,3,4,5]
# print(get_avg(test_list))

# 4-3
#입력 받는 값은 문자열로 나오기 때문에 숫자형으로 변경해서 계산
# input1 = int(input("첫번째 숫자를 입력하세요:"))
# input2 = int(input("두번째 숫자를 입력하세요:"))

# total = input1 + input2
# print("두 수의 합은 %s 입니다" % total)

#4-4
#3번만 문자열 사이에 공백이 있음

#4-5
local = "C:/Users/incom/OneDrive/바탕 화면/파이썬COP2/Mission/곽호준/test.txt"

#문서에 저장은 되나 print 출력이 안됨 => 문서 open 후 close 해줘야함
# f1 = open(local, 'w')
# f1.write("Life is too short")
# f1.close()

# f2 = open(local, 'r')
# print(f2.read())
# f1.close()

#4-6
# input = input("메모장에 저장할 내용을 입력해주세요 : " )
# with open(local, 'a') as f:
#     f.write(input)
# with open(local, 'r') as f:
#     print(f.read())

#4-7
# with open(local, 'r') as f:
#     before_msg = f.read()
#     print(before_msg)
#     new_msg = before_msg.replace('java', 'python')

# with open(local, 'w') as f:
#     f.write(new_msg)
#     print(new_msg)


