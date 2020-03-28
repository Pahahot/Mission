# 2-1 번
# 리스트 버전
# a="홍길동"
# b=[["국어",80], ["영어", 75], ["수학", 55]]
# c=0
# for i in range(len(b)):
#     c= c + b[i][1]
# print("%s의 평균은 %d 입니다." %(a, (c/len(b))))

# 딕셔너리 버전
# a="홍길동"
# b={"국어" : 80, "영어" : 75, "수학" : 55}
# c=0
# for i in b.values():
#     c= c + i
# print("%s의 평균은 %d 입니다." %(a, (c/len(b))))


#2-2
# a=13
# if a % 2 == 1:
#     print("%s는 홀수입니다." %a)
# else:
#     print("%s는 짝수입니다." %a)

#2-3 / 2-4
# Name="홍길동"
# b="881120-1068234"
# Year = b[:2]
# Month = b[2:4]
# Date = b[4:6]
# if b[7] == "1":
#     Sex = "남자"
# else:
#     Sex = "여자"
# print(f"{Name}는 {Year}년 {Month}월 {Date}일생 {Sex}입니다.")

#2-5
# Before = "a:b:c:d"
# After = Before.replace(':', '#')
# print(After)

#2-6
# list = [1, 3, 5, 4, 2];
# list.sort()
# list.reverse()
# print(list)

#2-7
# list = ['Life', 'is', 'too', 'short']
# a=""
# for i in range(len(list)):
#     a= a + list[i] + " "
# print(a)

# list = ['Life', 'is', 'too', 'short']
# print(" ".join(list))

#2-8
# tuple = (1,2,3)
# tuple2 = (4,)
# print(tuple+tuple2)

#2-9
# 3. key 값에는 리스트 사용 불가

#2-10
# a = {'A':90, 'B':80, 'C':70}
# print(a.get('B'))
# print(a)

# a = {'A':90, 'B':80, 'C':70}
# print(a.pop('B'))
# print(a)

#2-11
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# print(set(a))

#2-12
# a와 b가 동일한 리스트를 가리키고 있기 때문
# a = b = [1, 2, 3]
# a[1] = 4
# print(id(a))
# print(id(b))
# print(b)