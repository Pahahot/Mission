#8-1
# a ="a:b:c:d"
# print(a.split(":"))
# b = a.split(":")
# print("#".join(b))


#8-2
# a = {'A' : 90, 'B' : 80}
# if ('C' in a) == True:
#     print(a['C'])
# else:
#     print('70')

#8-3
# append를 이용하면 기존의 리스트에 항목 추가, 그냥 +를 쓰면 새로운 리스트를 만듬

#8-40
# a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# total = 0
# for i in a:
#     if i >= 50:
#         total += i

# print(total)

#8-5
# start_num = 0
# second_num = 1
# total = 1
# number=int(input("숫자를 입력하세요 : " ))

# if number == 1:
#     total = start_num
# elif number == 2:
#     total = second_num
# else:
#     for i in range(3,number+1):
#         next_num = start_num + second_num
#         start_num = second_num
#         second_num = next_num
#         total += next_num
# print(total)

#8-6
# input_list = input("숫자들을 입력하세요 : " )
# numbers = input_list.split(',')
# total = 0
# print(numbers)
# for i in numbers:
#     total += int(i)
# print(total)
    
#8-7
# input_number = int(input("구구단을 할 숫자를 입력하세요  " ))
# for i in range(1,10):
#     print(input_number * i, end = ' ')

#8-8  -> 분석이 필요
local = "C:/Users/incom/OneDrive/바탕 화면/파이썬COP2/Mission/곽호준/abc.txt"
local2 = "C:/Users/incom/OneDrive/바탕 화면/파이썬COP2/Mission/곽호준/num.txt"

with open(local, 'r') as f:
    content = f.readlines()

print(content)
content.reverse()
# print(content.reverse())

with open(local,'w') as f:
    for i in content:
        i = i.strip()
        f.write(i)
        f.write('\n')

#8-9
# total = 0
# with open(local2, 'r') as f:
#     content = f.readlines()

# print(content)
# for i in content:
#     total += int(i)

# print (total/len(content))

#8-10
# class Calculator:
#     def print_num(self, total):
#         print(total)

# class Calculate(Calculator):
#     def __init__(self, numList):
#         self.numList = numList

#     def add(self):
#         total = 0
#         for i in self.numList:
#             total += i
#         self.print_num(total)
#         return total
        
#     def avg(self):
#         total = self.add()
#         self.print_num(total/len(self.numList))

# cal1 = Calculate([1,2,3,4,5])
# cal1.add()
# cal1.avg()