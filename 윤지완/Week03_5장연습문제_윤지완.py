# 연습문제1
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, var):
        self.value += var

class UpgradeCalculator(Calculator):
    def minus(self, var):
        self.value -= var

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
print(' ')


# 연습문제2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()

cal.add(50)
print(cal.value)

cal.add(60)
print(cal.value)
print(' ')

# 부모 클래스에 있는 메소드를 메소드 오버라이딩하여
# 자식 클래스에도 구현하면 자식 클래스에 있는 메소드를 호출하게 된다


# 연습문제3
print(all([1, 2, abs(-3)-3]))
"""
위 문장은 False를 반환한다. all()은 안에 있는 반복가능한 인수형이 모두 참이여야 참을 반환하는데
abs[-3]-3 = 0(False)이기 때문에 False를 반환하게 된다.
"""

print(chr(ord('a')) == 'a')
print(' ')
"""
위 문장은 True를 반환한다.
ord : 문자의 아스키 코드값 반환
chr : 아스키 코드의 문자값 반환
"""


# 연습문제4
a = list(filter(lambda num: num>0, [1,-2,3,-5,8,-3]))
print(a)
print(' ')


# 연습문제5
num = int('0xea', 16)
print(num)

"""
int('A값', B진수)
B진수 A값을 10진수 값으로 반환
"""


# 연습문제6
list_a = list(map(lambda x: x*3, [1,2,3,4]))
print(list_a)
print(' ')


# 연습문제7
list_b = [-8,2,7,5,-3,5,0,1]
sum = max(list_b)+min(list_b)
print(sum)
print(' ')


# 연습문제8
result = round(17/3, 4)
print(result)
print(' ')


"""
# 연습문제9
import sys

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)
print(result)


# 연습문제10
import os
os.chdir("c:\doit")

result = os.popen("dir")

print(result.read())


# 연습문제11
import glob
glob.glob("c:\doit\*.py")
"""


# 연습문제12
import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))
print(' ')
# %Y:년, %m:월, %d:일, %H:시, %M:분, %S:초


# 연습문제13
import random

def lotto_plz():
    numbers = list(range(1, 46))

    for i in range(6):
        number = random.choice(numbers)
        numbers.remove(number)
        print("%d번째번호는 : "%(i+1), number)

lotto_plz()