#스택
import sys
input=sys.stdin.readline

stack=[]

for i in range(int(input())):
    cmd=list(input().split())
    if cmd[0]=='push':
        stack.append(cmd[1])
    elif cmd[0]=='pop':
            if stack:
                print(stack[-1])
                stack.pop()
            else:
                print(-1)
    elif cmd[0]=='size':
        print(len(stack))
    elif cmd[0]=='empty':
        print(0 if stack else 1)
    elif cmd[0]=='top':
        print(stack[-1] if stack else -1)