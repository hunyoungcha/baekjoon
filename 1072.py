#승률 공식==y/x*100
#해결 해볼것
#브루트포스는 안될듯
x,y=map(int,input().split())
x/=2
y/=2
cnt=0
my=x-y
p=round(my/x*100,1) #패배률 공식
print(p)
while True:
    cnt+=1
    x+=1
    print(p-my/x*100)
    print('cnt= ',cnt)
    if p-my/x*100>=1.0:
        break

print(cnt)
