a,b=map(str,input().split())
ra=a[::-1]
rb=b[::-1]
maxi=""
for i in range(3):
    if ra[i]>rb[i]:
        maxi=ra
        break
    if ra[i]<rb[i]:
        maxi=rb
        break
print(maxi)
