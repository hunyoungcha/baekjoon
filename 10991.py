floor = int(input())

for i in range(floor):
    print(" " * (floor-i-1),end='')
    print("* " * i + '*')