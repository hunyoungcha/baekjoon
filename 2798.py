n,m=map(int,input().split())
f=list(map(int,input().split()))
f_sum=0
la_pr=0
stop_point=0

for i in range(len(f)): 
    if stop_point==1: break
    for j in range(i+1,len(f)):
        if stop_point==1: break
        for k in range(j+1,len(f)):
            f_sum=f[i]+f[j]+f[k]
            if la_pr<f_sum and not f_sum>m:
                la_pr=f_sum
            if la_pr==m:
                stop_point=1
                break
print(la_pr)