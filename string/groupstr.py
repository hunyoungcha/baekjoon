num=int(input())
count=0

for _ in range(num):
    str_var=input()
    error=0
    for index in range(len(str_var)-1):
        if str_var[index] != str_var[index+1]:
            new_str=str_var[index+1:]
            if new_str.count(str_var[index])>0:
                error+=1
    if error==0:
        count+=1        
print(count)