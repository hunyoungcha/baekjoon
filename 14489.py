a, b = map(int,input().split())
c= int(input())

c*=2
result = a+b 

if result >= c:
    print(result - c)
else:
    print(result)