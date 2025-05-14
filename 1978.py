n= int(input())
numlist = map(int,input().split())



def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

cnt =0
for i in numlist:
    if is_prime(i):
        cnt +=1
print(cnt)