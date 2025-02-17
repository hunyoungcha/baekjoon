n,m = map(int,input().split())

#n 리스트 :
nlist = []
for i in range(n):
    nlist.append(int(input()))

#m 리스트
mlist = []
for i in range(m):
    mlist.append(int(input()))

result = [0] * n

for ml in mlist:
    for idx,nl in enumerate(nlist):
        if ml >= nl:
            result[idx]+=1
            break

print(result.index(max(result))+1)