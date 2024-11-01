#덩치

n=int(input())
f=[]

rank=[1 for i in range(n)]

for i in range(n):
    w,h=map(int,input().split())
    f.append([w,h])

for i in range(len(f)):
    for j in range(len(f)):
        if (f[i][0] < f[j][0] and f[i][1] < f[j][1]):
            rank[i]+=1

print(' '.join(map(str,rank)))
