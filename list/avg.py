num=int(input()) #num변수에 정수형 input받아 저장
for i in range(num): # num만큼 반복
    count=0 #count변수를 0으로 초기화
    a=list(map(int,input().split())) # a변수에 정수형 input을 받아 공백을 기준으로 잘라 list로 저장
    avg=sum(a[1:])//a[0] #avg변수에 a의 1번부터 끝까지 더해 a[0]으로 나눈 값을 저장
    for j in range(1,len(a)): #a의 길이만큼 반복
        if a[j]>avg: 
            count+=1
    print("{:.3F}%".format(round(count/a[0]*100,3))) #퍼센트 구한값을 반올림해 셋째 자리까지 출력