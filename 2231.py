n=int(input())
str_n=""

count=n//2

while True:
    n_sum=0
    if count>n:
        print("0")
        break
    for i in str(count):
        n_sum+=int(i)
    if count+n_sum==n:
        print(count)
        break
    count+=1
    