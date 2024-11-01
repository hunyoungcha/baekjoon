import heapq

def insert(num):
    heapq.heappush(max_q,-num)
    heapq.heappush(min_q,num)

def delete(num):
    if num==1:
        heapq.heappop(max_q)
        heapq.heappop(-min_q)


a=int(input())
for i in range(a):
    b=int(input())
    max_q=[]
    min_q=[]
    for j in range(b):
        id,num=map(str,input().split())
        num=int(num)
        if id=='I':
            insert(num)
        elif id=='D':
            delete(num)
    if len(q)!=0:
        print(f'{max(q)} {min(q)}')
    else:
        print('EMPTY')