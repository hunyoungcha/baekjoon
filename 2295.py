n=int(input())

#a+b+c==d 
#a+b==d-c로 바꾸기 가능

s=set()
for i in range(n):
    s.add(int(input()))


#a+b의 모든 경우의 수 값을 저장하는 집합 만들기
sum_s=set()
for i in s:
    for j in s:
        sum_s.add(i+j)

#d-c의 값이 a+b집합에 있는지 비교

result=set()
for i in s:
    for j in s:
        if (i-j) in sum_s:
            result.add(i)

result=sorted(list(result),reverse=True)
print(result[0])