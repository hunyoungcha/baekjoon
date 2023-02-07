alp=input()
ualp=alp.upper()
num_list=[0]*26
alp_num=65
for i in range(alp_num,91):
    for j in ualp:
        if chr(i)==j:
            num_list[i-alp_num]+=1

sort_list=sorted(num_list)
if sort_list[-1]== sort_list[-2]:
    print("?")
else: 
    print(chr(int(num_list.index(max(num_list))+alp_num)))