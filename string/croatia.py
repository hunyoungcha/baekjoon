alp_list=["dz=","c=","c-","d-","lj","nj","s=","z="]
alp=input()

for i in alp_list:
    alp=alp.replace(i,'*')
print(len(alp))