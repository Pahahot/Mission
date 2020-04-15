#01
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -=val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


#02
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100



#03
all([1, 2, abs(-3)-3])
chr(ord('a')) == 'a'


#04
list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))

#05
int('0xea', 16)

#06
 list(map(lambda x:x*3, [1,2,3,4]))


 #07

a = [-8, 2, 7, 5, -3, 5, 0, 1]
max(a) + min(a)


#08
 round(17/3, 4)

 #09
import sys

numbers = sys.argv[1:] 
result = 0
for number in numbers:
    result += int(number)
print(result)


#10
import os
os.chdir("c:/doit")
result = os.popen("dir")

print(result.read())


#11
import glob
glob.glob("c:/doit/*.py")


#12
import time
time.strftime("%Y/%m/%d %H:%M:%S")   

#13
import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)   
    if num not in result:
        result.append(num)

print(result)
