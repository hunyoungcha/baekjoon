num=int(input())
for i in range(num):
    a,b=map(str,input().split())
    for j in range(len(b)):
        for k in range(int(a)):
            print(b[j],end="")
    print()