# 6-2. 3과 5의 배수 합하기

sum = 0
for n in range(1, 1000) :
    if n % 3 == 0 or n % 5 == 0 :
        sum += n

print(sum)


# 6-3. 게시판 페이징하기
def getTotalPage(m, n) :
    TotalPage = 0
    if m % n == 0 :
        TotalPage = m // n
    else :
        TotalPage = m // n + 1
    
    return TotalPage

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))


