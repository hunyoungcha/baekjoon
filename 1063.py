#65~72 : A~H
#해결해볼것

from pprint import pprint




k,s,n=map(str,input().split())
n=int(n)

board=[[0 for i in range(8)] for j in range(8)]
board[int(k[1])-1][ord(k[0])-65]=1
board[int(s[1])-1][ord(s[0])-65]=2
board=board[::-1]
pprint()
    

# for i in range(n):
#     q=input()
#     tmp_board=board
#     k0=ord(k[0])
#     k1=int(k[1])

#     if 'R' in q:
#         k0+=1
#         if k0>72:
#             k0-=1
#     elif 'L' in q:
#         k0-=1
#         if k0<65:
#             k0+=1
    
#     if 'B' in q:
#         k1-=1
#         if k1<1:
#             k1+=1
#     elif 'T' in q:
#         k1+=1    
#         if k1>8:
#             k1-=1


#     k=chr(k0)+str(k1)


