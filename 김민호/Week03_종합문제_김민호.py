#01
str1 = ("a:b:c:d")
print(str1)
result = " "
result = str1.split(":")
print(result)
result = "#".join(str1.split(":"))
result


#02
a = {'A':90, 'B':80}
a['C']

a.get('C',70)


#03
a = [1,2,3]
id(a)
a = a +[4.5]
a
id(a)     #주소값 4360931040
a = [1,2,3]
id(a)
a.extend([4,5])
a
id(a)     #주소값 430932000 extend로 했을 시 주소값이 그대로 동일 하지만 '+'햇을시 주소값이 달라짐



#04
A = [20,55,67,82,45,33,90,87,100,25]
sum = 0
for i in A:
    if i>=50:
        sum+=i
print(sum)

#05
def fibo(n):
    if n==0: return 0
    if n==1: return 1
    return fibo(n-2)+fibo(n-1)

a = fibo(5)


#06
number = input()
sp = number.split(",")
sum = 0
for i in sp:
        sum +=int(i)
print(sum) 



#07
user_input = input("구구단을 출력할 숫자를 입력하세요: ")
dan = int(user_input)
for i in range(1,10):
    print(dan*i)


#08
f = open('abc.txt', 'r')
lines = f.readlines()    # 모든 라인을 읽음
f.close()

lines.reverse()          # 읽은 라인을 역순으로 정렬

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()  # 포함되어 있는 줄 바꿈 문자 제거
    f.write(line)
    f.write('\n')        # 줄 바꿈 문자 삽입
f.close()


#09
f = open("sample.txt")
lines = f.readlines( )  
f.close( )

total = 0
for line in lines:
    score = int(line)  
    total += score
average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()


#10
class Calculator:
    def init(self, numberlist):
        self.numberlist = numberlist

    def add(self): result = 0
        for num in self.numberlist:
            result += num
        return result
    def avg(self):
        total = self.add()
        return total / len(self.numberList)


