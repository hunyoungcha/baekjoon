q=int(input())

for i in range(q):
    fl=int(input())
    ho=int(input())
    fo=[q for q in range(1,ho+1)] #0층의 거주민의 수 리스트
    for j in range(fl):
        for k in range(1,ho): #1부터 시작하는 이유: fo[0]은 항상 1이기 때문에
            fo[k]=fo[k]+fo[k-1] #fo[k]위치에 k와 k-1을 계속 더해 저장한다 
    print(fo[-1]) #가장 큰 수를 출력
