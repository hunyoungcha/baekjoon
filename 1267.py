n= int(input())
time = list(map(int,input().split()))

def calc(time, key) :
    k = 30 if key == "y" else 60
    money = 10 if key =="y" else 15
    result = 0
    
    for t in time:
        cnt = 0
        tmp = t / k

        if tmp != int(tmp) or t%k == 0:
            cnt +=1
        
        cnt += int(tmp)
        result += money * cnt

    return result

y=calc(time, "y")
m=calc(time, "m")

if y < m : 
    print(f"Y {y}")
elif m < y : 
    print(f"M {m}")
else : 
    print(f"Y M {y}")