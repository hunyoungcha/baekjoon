real_list=[]
sum_list=[]
num=10000
for i in range(1,num+1):
    for j in str(i):
        
        sum_list.append(j)
    hop=0
    for k in sum_list:
        hop+=int(k)
    hop+=i
    real_list.append(hop)
    sum_list=[]
for i in range(1,num+1):
    if not i in real_list:
        print(i)