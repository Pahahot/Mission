#2장 연습문제

#01
list = [80,75,55]
result = (list[0]+list[1]+list[2])/3
print(result)


#02
number = 13
if number/13 == 0 :
    print("짝수")
else:
    print("홀수")


#03
홍길동 = "881120-1068234"
print(홍길동.split("-"))

#04
pin = "881120-1068234"
print(pin[7])


#05
a= "a:b:c:d"
print(a.replace(":","#"))

#06
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#07
list = ['Life','is','too','short']
result = " ".join(list)
print(result)

#08
tp1 = (1,2,3)
tp2 = (4,)      #튜플은 한개만 쓸땐 콤마(,)를 붙여야함
result  = tp1 + tp2 
print(result)

#09

a= dict()
a
a['name'] = 'python'
a[('a',)] = 'python'
#a[[1]] = 'python'   딕셔너리에 key값으로 튜플은 넣을수 있지만 리스트는 넣을 수 없음
a[250] = 'python'

print(a)


#10
a  = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(result)

#11   집합자료형은 중복이 안되고 무작위로 추출됨
a= [1,1,1,2,2,2,3,3,3,4,4,5]
result = set(a)
print(result)


#12
a= b= [1,2,3]
a[1 ] = 4
print(b)     #동일한 값이 나오는 이유는 동일한 주소값을 가지고 있기 때문에
