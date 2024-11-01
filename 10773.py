n=int(input())
snum=[]
for i in range(n):
    num=int(input())
    if num==0:
        snum.pop()
    else:
        snum.append(num)
print(sum(snum))