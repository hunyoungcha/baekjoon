hole,bupi=map(int,input().split())
a=list(map(int,input().split()))
sum_j=0
minus_bupi=0
max_sum=0
sma_bupi=bupi

for i in range(hole): #시작점 고르기
    for j in a[i:]: 
        minus_bupi=bupi-j
        sum_j+=j

        if minus_bupi<0:
            break
        elif minus_bupi==0 or 

        if sma_bupi>minus_bupi:
            sma_bupi=minus_bupi        