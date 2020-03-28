#3장 연습문제 풀이

#01
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else : print("none")

#답 shirt ---세번째 줄에서 참이므로 빠져놔와 그 이후 문장은 실행되지 않음


#02
a = 1
number =0
while a<=1000 :
    if a%3==0 :
        number +=a
    a +=1
print(number)


#03
a = 1
while a<=5:
    print("*" *a)
    a+=1

#04
for i in range(1,101) :
    print(i)


#05
ClassA = [70,60,55,75,95,80,80,85,100]
b= len(ClassA)
sum = 0
for i in range(0,b):   
    sum += ClassA[i]
print(sum/len(ClassA))


#06
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)