num=int(input())

a=[]
for i in range(num):
    a.append(list(map(int,input().split())))

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None