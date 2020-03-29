# 연습문제1
a = 80
b = 75
c = 55
avg = ((a+b+c)/3)
print(avg)


# 연습문제2
number = 29
if number%2==0 :
    print("짝수")
else :
    print("홀수")


# 연습문제3
JuminNumber = '881120-1068234'

# 방법1
YMD = JuminNumber[:6]
etc = JuminNumber[7:]
print(YMD)
print(etc)

# 방법2
print(JuminNumber.split('-'))


# 연습문제4
print(JuminNumber[7])


# 연습문제5
a = "a:b:c:d"
print(a.replace(':','#'))


# 연습문제6
list_a = [1,3,5,4,2]
list_a.sort()
list_a.reverse()
print(list_a)


# 연습문제7
list_b = ['Life', 'is', 'too', 'short']
print(" ".join(list_b))


# 연습문제8
t1 = (1,2,3)
print(t1 + (4,)) # 튜플은 한 개의 요소만 가질 때 요소 뒤에 반드시 콤마(,)!


# 연습문제9
a = dict()
a['name'] = 'python'
a[('a',)] ='python'
# a[[1]] = 'python'
a[250] = 'python'

"""
a[[1]] = 'python'을 수행할 때 오류가 발생한다
리스트는 변할 수 있는 값이다. 딕셔너리에서 키는 변할 수 없는 값만 가능하다.
"""


# 연습문제10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))


# 연습문제11
a = [1,1,1,2,2,3,3,3,4,4,5]
b = set(a)
print(b)


# 연습문제12
a = b = [1,2,3]
a[1] = 4
print(b)

"""
print(b)를 하면 [1,4,3]이 출력된다.
a = b = [1,2,3] 을 하면 a와 b가 완전히 동일한 객체를 가리키고 있다.
따라서  a[1] = 4 를 하게 되면 리스트 a가 [1,4,3]을 가리키게 되고
b 역시 [1,4,3] 리스트를 가리키게 된다.