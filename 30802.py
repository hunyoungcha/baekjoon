n= int(input())
s = map(int,input().split())
t,p = map(int,input().split())


sresult = 0

for i in s:
    sresult += i//t
    if i%t != 0 : sresult+=1

print(sresult)
print(f"{n//p} {n%p}")