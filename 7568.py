n=int(input())
f=[[0]*2 for i in range(n)]
sc=[0* i for i in range(n)]

for i in range(n):
    x,y=map(int,input().split())
    for j in range(2):
        f[i][0]=x
        f[i][1]=y

