num = list(map(int,input().split()))

q = 0
for i in num:
    q+= i**2

print(q%10)