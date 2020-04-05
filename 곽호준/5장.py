#5-1
# class Calculator:
#     def __init__(self):
#         self.value = 0
    
#     def add(self, val):
#         self.value += val
    
#     def minus(self, val):
#         self.value -= val

# class UpgradeCalculator(Calculator):
#     pass


# cal =UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)

#5-2
# class Calculator:
#     def __init__(self):
#         self.value = 0
    
    # 버전 1 용
    # def add(self, val):
    #     if val >= 50:
    #         val = 50
    #     self.value += val

    #버전 2용
    # def add(self, val):
    #     val = self.maxcheck(val)
    #     self.value += val
# 버전 1용
# class MaxlimitCalculator(Calculator):
    # pass

#버전 2용
# class MaxlimitCalculator(Calculator):
#     def maxcheck(self, value):
#         if self.value >= 50:
#             value = 50
#         return value

# cal = MaxlimitCalculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)

#5-3
#1. abs(-3) => 3 => 3-3 = 0 => all[1,2,0] => 0 때문에 false
#2. chr함수의 반대는 ord => a는 그대로 a가 됨으로 true

#5-4
# def minuscheck(number):
#     if number > 0:
#         return number

# print(filter(minuscheck, [1, -3, 2, 0, -5, 6]))

# print(list(filter(minuscheck, [1, -3, 2, 0, -5, 6])))

# print(list(filter(lambda number: number > 0, [1,-3,2,0,-5,6])))

#5-5
# print(int('0xea', 16))

#5-6
# def test(number):
#     return number * 3

# print(list(map(test, [1,2,3,4])))
# print(list(map(lambda number: number * 3, [1,2,3,4])))

#5-7
# list = [-8, 2, 7, 5, -3, 5, 0, 1]
# print(max(list) + min(list))

#5-8
# print(round(17/3,4))

#5-9
# import sys

# numbers = sys.argv[1:]
# print(numbers)

# result=0
# for i in numbers:
#     result += int(i)

# print(result)

#5-10
# import os
# os.chdir("C:/Users")
# f = os.popen("dir")
# print(f.read())

#5-11
# import glob
# import os

# f=os.popen("dir")
# print(f.read())
# print("=" * 30)
# print(glob.glob("C:/Users/incom/OneDrive/바탕 화면/파이썬COP2/Mission/곽호준/*.py"))

#5-12
# import time
# print(time.localtime(time.time()))
# print(time.localtime())
# print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))

#5-13
# import random
# result = []

# while len(result) < 6:
#     number = random.randint(1,45)
#     if number not in result:
#         result.append(number)

# print(result)

