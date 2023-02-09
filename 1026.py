a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))

b=sorted(b)
c=sorted(c,reverse=True)
cnt=0
for i in range(a):
    cnt+=(b[i]*c[i])

print(cnt)