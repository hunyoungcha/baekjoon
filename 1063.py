k,s,n=map(str,input().split())
n=int(n)






for i in range(n):
    q=input()
    tmp_k=k
    k0=ord(k[0])
    k1=int(k[1])

    if 'R' in q:
        k0+=1
    elif 'L' in q:
        k0-=1
    
    if 'B' in q:
        k1-=1
    elif 'T' in q:
        k1+=1    
    k=chr(k0)+str(k1)

print(k)
