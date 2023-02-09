#공포도가 x인 사람은 x명 이상 모여야 팀이 가능하다
#ex) 1 2 3 2 2 --> 123 || 22

q=int(input())
peo=list(map(int,input().split()))

print(sorted(peo)) 