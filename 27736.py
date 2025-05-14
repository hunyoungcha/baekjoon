n = int(input())
l = list(map(int,input().split()))

a= l.count(1)
r= l.count(-1)
i= l.count(0)

if i >= (n//2) + (n%2) :
    print("INVALID")
elif r >= a:
    print("REJECTED")
else :
    print("APPROVED")