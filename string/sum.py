count=int(input())
num=input()
nlist=[]
nsum=0
for i in num:
    nlist.append(i)
a=map(int,nlist)
b=sum(a)
print(b)