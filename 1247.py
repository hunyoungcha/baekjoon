from sys import stdin

for i in range(3):
    numSum = 0
    num = int(stdin.readline())

    for j in range(num):
        n = int(stdin.readline())
        numSum+= n
    
    if numSum > 0:
        print("+")
    elif numSum == 0:
        print("0")
    else:
        print("-")