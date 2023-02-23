def D(num):
    global q
    if len(q)!=0:
        if num=='1':
            q.remove(max(q))
        elif num=='-1':
            q.remove(min(q))


def I(num):
    global q
    q.append(int(num))


a=int(input())
for i in range(a):
    b=int(input())
    q=[]
    for j in range(b):
        id,num=map(str,input().split())
        if id=='I':
            I(num)
        elif id=='D':
            D(num)
    if len(q)!=0:
        print(f'{max(q)} {min(q)}')
    else:
        print('EMPTY')