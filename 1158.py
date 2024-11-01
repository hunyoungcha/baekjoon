a,b=map(int,input().split())
person=[i for i in range(1,a+1)]
result=[]

idx=b-1
while person:
    while idx >= len(person):
        idx-=len(person)
    result.append(person[idx])
    person.pop(idx)
    idx=idx+b-1
    
print("<{}>".format(', '.join(map(str,result))))