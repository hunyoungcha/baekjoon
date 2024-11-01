import sys
input=sys.stdin.readline

n=int(input())
d=[]

for i in range(n):
    cmd=list(input().split())
    if cmd[0]=='push_front':
        d.insert(0,cmd[1])
    elif cmd[0]=='push_back':
        d.append(cmd[1])
    elif cmd[0]=='pop_front':
        print(d.pop(0) if d else -1)
    elif cmd[0]=='pop_back':
        print(d.pop()) if d else print(-1)
    elif cmd[0]=='size':
        print(len(d))
    elif cmd[0]=='empty':
        print(0 if d else 1)
    elif cmd[0]=='front':
        print(d[0] if d else -1)
    elif cmd[0]=='back':
        print(d[-1] if d else -1)