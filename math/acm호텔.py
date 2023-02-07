q=int(input())
for i in range(q):
    h,w,n=map(int,input().split())
    f=0
    d=0
    if n%h==0:
        f=h*100
        d=n//h
    else:
        f=n%h*100
        d=n//h+1
    print(f+d)

#나머지는 층수, 나눈 몫은 동수가 된다
#나머지가 없을 경우 가장 위층이 되고 몫 그대로 동수가 된다
#나머지가 있을경우 몫의 +1한 수가 동수가 된다