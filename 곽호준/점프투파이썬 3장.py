#3-1
# shirt 출력 
# (wife 없음, python은 있으나 you도 있음, shirt 없음, 
# short 조건에 걸려서 아래는 패스)

#3-2
# i=1
# total = 0
# while i <= 1000:
#     if i % 3 == 0:
#         total = total + i
#     i = i + 1

# print(f"1부터 1000까지의 3의 배수의 총 합은 {total} 입니다.")

#3-3
#for문
# for i in range(6):
#     print("*" * i)

#while문
# i=1
# while i <= 5:
#     print("*" * i)
#     i = i + 1

#3-4
# for i in range(1, 101):
#     print(i)

#3-5
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# total2 = 0

# for i in A:
#     total = total + i

# print(total/len(A))
# print(total//len(A))

# for i in range(len(A)):
#     total2 = total2 + A[i]
# print(total2/len(A))

#3-6
# numbers = [1, 2, 3, 4, 5]

# result = [n * 2 for n in numbers if n % 2 ==1]

# print(result)