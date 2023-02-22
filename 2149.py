#https://www.acmicpc.net/board/view/28285
#부분점수, 준비 다 되고 시간 남으면 풀어보기

key=input()
inc=input()

row=len(inc)//len(key)
lkey=sorted(key)


f=[]
cnt=0
num=row
for i in lkey:
    x=i
    for j in range(cnt,num):
        x+=inc[j]
    cnt=j+1
    num+=row
    f.append(x)

fin=[]
for i in key:
    for j in f:
        if i==j[0]:
            fin.append(j)
            break

# result=''
# for i in range(1,row+1):
#     for j in range(len(fin)):
#         result+=fin[j][i]
# print(result)

print(fin)
