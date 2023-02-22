#97~122

def dec(code,cnt):
    tmp=''
    for i in code:
        q=ord(i)+cnt
        if q>122: 
            q=q-122+96
        tmp+=chr(q)
    return tmp

def check(tmp,keyword):
    for i in keyword:
        if i in tmp:
            return True

code=input()
num=int(input())

keyword=[]
for i in range(num):
    keyword.append(input())

c=0
while True:
    dec_str=dec(code,c)
    c+=1
    if check(dec_str,keyword)==True:
        print(dec_str)
        break
    elif c>25:
        break
    
