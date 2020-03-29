# 연습문제1

# 방법1
def is_odd(num):
    if num % 2 == 0:
        return '짝수'
    else:
        return '홀수'

print(is_odd(3))
print(is_odd(4))

# 방법2
is_odd = lambda num: '짝수' if num%2 == 0 else '홀수'

print(is_odd(3))
print(is_odd(4))


# 연습문제2
def avg(*args) :
    sum = 0
    for i in args:
        sum += i

    return sum/len(args)

print("평균 : " + str(avg(1,3,5,7,9)))


# 연습문제3
input1 = input("첫번째 숫자를 입력하세요: ")
input2 = input("두번째 숫자를 입력하세요: ")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." % total)


# 연습문제4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")   # 콤마가 있으면 공백이 삽입
print("".join(["you", "need", "python"]))


# 연습문제5
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


# 연습문제6
input3 = input("내용 입력 : ")
f3 = open("test.txt",'a')
f3.write(input3)
f3.close()


# 연습문제7
f= open("test.txt",'r')
a = f.read()
f.close()

a = a.replace("java","python")
f = open("test.txt",'w')
f.write(a)
f.close()
