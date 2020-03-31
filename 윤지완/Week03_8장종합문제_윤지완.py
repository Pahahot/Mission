# 종합문제1

# split, join 사용하지 않았을 때
s = 'a:b:c:d'
change_s = s.replace(':','#')
print(change_s)

# join 사용하였을 때
s = 'a:b:c:d'
change_s = s.split(':') # 쪼개진 결과는 리스트에 저장
result = '#'.join(change_s)
print(result)


# 종합문제2
a = {'A':90, 'B':80}
print(a.get('C', 70))

# 딕셔너리에서 get(x, 'default')를 사용하면 Key값이 없으면 'default'값 불러온다.


# 종합문제3
# 해당 내용은 잘 몰라서 풀이를 참조함

# + 사용
a = [1, 2, 3]
print(id(a))
a = a + [4, 5]
print(id(a))
print(a)
"""
기존 a = [1, 2, 3]에 +를 이용하여 [4, 5]를 연결하면
a 는 새로운 리스트를 반환하게 된다.
id(a)의 값이 달라짐
"""


# extend 사용
a = [1, 2, 3]
print(id(a))
a.extend([4,5])
print(id(a))
print(a)
"""
기존 a를 extend 하여 [4, 5]를 추가하면
a 는 기존 리스트 그대로의 주소값 반환
"""


# 종합문제4

# 방법1
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for num in A :
    if num >= 50:
        sum += num
    else:
        continue

print(sum)

# 방법2
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
while A:
    num = A.pop()
    if num >= 50:
        sum += num

print(sum)


# 방법3
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
a_50_up = list(filter(lambda num: num >= 50, A))
for i in a_50_up:
    sum += i
print(sum)


# 종합문제5
def fibo(num) :
    if num == 0: return 0
    if num == 1: return 1
    return fibo(num-2) + fibo(num-1)

num = int(input("양의 정수를 입력해 보아용 : "))
for i in range(num) :
    print(fibo(i), end=" ")
print(' ')


# 종합문제6
numbers = input("숫자 입력 : ")
list_num = numbers.split(',')
sum = 0
while list_num:
    num = list_num.pop()
    sum += int(num)
print(sum)


# 종합문제7
dan = int(input("구구단을 출력할 숫자를 입력하세요(2~9): "))
for i in range(1,10):
    print(i*dan, end=" ")

print(' ')


"""
# 종합문제8
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')

f.close()


# 종합문제9
f = open('sample.txt')
lines = f.readlines()
f.close()

sum = 0
for line in lines:
    jumsu = int(line)
    sum += jumsu
avg = sum / len(lines)

f = open('result.txt', 'w')
f.write(str(avg))
f.close()
"""


# 종합문제10
class Calculator:
    def __init__(self, numList):
        self.numList = numList
    
    def add(self):
        sum = 0
        for i in self.numList:
            sum += i
        return sum
    
    def avg(self):
        return self.add() / len(self.numList)


cal1 = Calculator([1,2,3,4,5])
cal2 = Calculator([6,7,8,9,10])

print(cal1.add())
print(cal1.avg())
print(cal2.add())
print(cal2.avg())