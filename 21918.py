l, c = map(int,input().split())

light = list(map(int,input().split()))

def command(cmd1, cmd2, cmd3):
    if cmd1 == 1 :
        light[cmd2-1]=cmd3
    elif cmd1 == 2 :
        for i in range(cmd2-1, cmd3, 1):
            light[i] = 1 if light[i] ==0 else 0

    elif cmd1 == 3:
        for i in range(cmd2-1, cmd3):
            light[i]=0

    elif cmd1 == 4:
        for i in range(cmd2-1, cmd3):
            light[i]=1


for _ in range(c):
    cmd1, cmd2, cmd3 = map(int,input().split())
    command(cmd1,cmd2,cmd3)

print(' '.join(map(str,light)))