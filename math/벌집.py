n=int(input())
first=1 
num=6
room=1
if n==1:
    print(1)
else:
    while True:
        first+=num 
        room+=1
        if n <=first: 
            print(room)
            break
        num+=6

#숫자: [2~7] [8~19] [20~37] ...
#갯수: 6      12     18     ...
#first변수에 6의 배수를 더해주면서 제일 큰 숫자보다 n이 작아지면 room을 출력한다