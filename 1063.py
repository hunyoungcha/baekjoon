#65~72 : A~H
#해결
k,s,n=map(str,input().split())
n=int(n)

k=[ord(k[0]),int(k[1])]
s=[ord(s[0]),int(s[1])]

for i in range(n):
    com=input()
    tmp_k=k.copy() #그냥 다른 변수에 넣으면 메모리 주소를 그대로 복사하기 때문에 값도 같이 변경 됨, COPY명령어를 통해 다른 메모리에 저장
    tmp_s=s.copy()
    #커맨드 이동 명령
    if 'R' in com:
        k[0]+=1
    elif 'L' in com:
        k[0]-=1
    if 'T' in com:
        k[1]+=1
    elif 'B' in com:
        k[1]-=1

    if k[0]==73 or k[0]==64 or k[1]==0 or k[1]==9:
        k=tmp_k
    if k==s:
        if tmp_k[0]-k[0]==-1:
            s[0]+=1
        elif tmp_k[0]-k[0]==1:
            s[0]-=1
        if tmp_k[1]-k[1]==-1:
            s[1]+=1
        elif tmp_k[1]-k[1]==1:
            s[1]-=1
        if s[0]>72 or s[0]<65 or s[1]<1 or s[1]>8:
            k=tmp_k
            s=tmp_s

print(chr(k[0])+str(k[1]))
print(chr(s[0])+str(s[1]))