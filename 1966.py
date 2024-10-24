#프린터 큐
from collections import deque as dq

n=int(input())

for i in range(n):
    lgt,me=map(int,input().split())
    f=dq(map(int,input().split()))
    soon={i:1  for i in range(lgt)}
print(soon[me])

#soon은 인덱스 별로 우선순위
#deque 써서 할것