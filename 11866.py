from collections import deque

n, k = map(int,input().split())
dq = deque()
[dq.append(i) for i in range(1,n+1)]

print("<", end="")
while True:
    if len(dq) == 1:
        print(f"{dq.popleft()}>")
        break
    dq.rotate(-k+1)
    print(f"{dq.popleft()}, ", end="")
