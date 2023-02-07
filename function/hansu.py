k=int(input())
hansu=0
for i in range(1,k+1):
    q=list(map(int,str(i)))
    if i<100:
        hansu+=1
    elif q[0]-q[1] == q[1]-q[2] :
        hansu+=1
print(hansu)