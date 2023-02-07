num=int(input())

for i in range(num):  
    count=0
    a=list(input().split("X"))
    a=list(filter(None,a))
    for j in a:
        for k in range(1,len(j)+1):
            count+=k
    print(count)