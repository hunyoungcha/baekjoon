alp=list(input())
num_list=[-1]*26
for i in range(97,123):
    for j in range(len(alp)):
        if num_list[i-97] ==-1:
            if chr(i) == alp[j]:
                num_list[i-97]=j           
for i in num_list:
    print(int(i),end=" ")