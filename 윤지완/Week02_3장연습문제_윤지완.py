# 연습문제1
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# shirt만 출력된다. 앞에 2개 조건은 False 이고
# 3번째 조건이 True 이므로 3번째 조건 만족 후 이후 문장 실행 X


# 연습문제2
sum = 0
number = 0
while number < 1000:
    number += 1
    if number % 3 != 0:
        continue
    sum += number

print(sum)


# 연습문제3

# 방법1, 2중 반복
i = 1
j = 0
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print(' ')
    i += 1

# 방법2
i = 1
while i <= 5:
    print("*" * i)
    i += 1


# 연습문제4
for i in range(1, 101) :
    print(i)


# 연습문제5

# 방법1
list_jumsu = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for jumsu in list_jumsu :
    sum += jumsu
print(sum / len(list_jumsu))

# 방법2
l = len(list_jumsu)
sum = 0
for i in range(0, l) :
    sum += list_jumsu[i]
print(sum / l)


# 연습문제6
# 리스트 내포 사용 전
numbers = [1,2,3,4,5]
result = []
for n in numbers :
    if n % 2 == 1 :
        result.append(n*2)
print(result)

# 리스트 내포 사용 후
result = [num * 2 for num in numbers if num % 2 == 1]
print(result)
