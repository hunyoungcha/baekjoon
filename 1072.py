#승률 공식==y/x*100
#해결 해볼것



# 승률 구하는 방법
# x,y=map(int,input().split())
# cnt=-1


# while x!=y:
#     cnt+=1
#     y+=1
#     x+=1
#     stop_p=(y/x*100+1.0)/100*x/y
#     if 1>=stop_p:
#         cnt+=1
#         break

# print(cnt)

x,y=map(int,input().split())
z=y*100//x
start,end=0,1000000000

if z>=99:
    print(-1)
else:
    while

















# xy=x-y
# half_x=x//100
# goal=(xy/x*100-1.0)/100
# cnt=0
# if x==y:
#     cnt-=1
# elif xy/(x+half_x) >= goal:
#     x=half_x+x
#     cnt=half_x

# while x!=y:
#     if xy/x <= goal:
#         break
#     cnt+=1
#     x+=1
# print(cnt)