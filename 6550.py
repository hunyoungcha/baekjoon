#kmp 알고리즘 문제
#https://bowbowbow.tistory.com/6

s,t=map(str,input().split())
idx=0
result='No'
for i in t:
    if i==s[idx]:
        idx+=1
        if idx == len(s):
            result='Yes'
            break
print(result)