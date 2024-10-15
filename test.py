q = int(input())

w = list(map(int,input().split()))
e = list(map(int,input().split()))

cnt=0

for i in range(q):
    if w[i] <= e[i] : cnt+=1

print(cnt)