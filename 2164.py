from collections import deque

dq = deque()
n = int(input())

[dq.append(i) for i in range(1,n+1)]

while len(dq) != 1:
    dq.popleft()
    q= dq.popleft()
    dq.append(q)

print(dq.pop())