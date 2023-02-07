dial=input()
num_list=["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]   #index
sum_num=0
for i in dial:
    for j in num_list:
        if i in j:
            sum_num+=num_list.index(j)+1
print(sum_num)