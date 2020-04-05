#4장 연습문제

#01

def is_odd(number) :
    if number %2 ==1 :
        print("홀수")
    else:
        print("짝수")


#02
def avg(*args):
    sum = 0
    for i in args :
        sum +=i
    result = 0
    result = sum/len(args)
    return result

print(avg(1,2,3,4,5))


#03

input1 = input("첫번째 숫자를 입력하세요 : ")
input2 = input("두번째 숫자를 입력하세요 : ")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다. " % total)

#04
print("you" "need" "python")
print("you" + "need" +"python")
print("you", "need", "python")    #컴마는 띄어쓰기로 인식
print("".join(["you","need","python"]))

#05

f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


#06
input3 = input("내용 입력 : ")
f3 = open("test.txt",'a')
f3.write(input3)
f3.close()


#07
f= open("test.txt",'r')
a = f.read()
f.close()

a = a.replace("java","python")
f = open("test.txt",'w')
f.write(a)
f.close()