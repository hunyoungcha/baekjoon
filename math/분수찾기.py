#타임 오버 실패

x=1
y=1
x_change=3
y_change=2
switch=0

iput=int(input())
if iput!=1:
    for i in range(1,iput):
        if y==y_change:
            switch=1
            y_change+=2
        elif x==x_change:
            switch=0
            x_change+=2

        if switch==0:
            y+=1
            x-=1
        elif switch==1:
            y-=1
            x+=1
        
        if x==0:
            x+=1
        elif y==0:
            y+=1        
print("{}/{}".format(x,y))