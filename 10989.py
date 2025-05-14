# import sys
# input=sys.stdin.readline

# n = int(input())

# l = [0] * 10001

# for i in range(n):
#     l[int(input())] += 1

# for i in range(10001):
#     for j in range(l[i]):
#         print(i)


# d = {key: 0 for key in range(10001)}

# for i in range(n):
#     d[int(input())] += 1

# for key in d.keys():

#     print(f"{key}\n" * d[key], end="")


import sys
n = int(sys.stdin.readline())

l =[0] * 10001

for i in range(n):
    l[int(sys.stdin.readline())] += 1

for idx,value in enumerate(l):
    for j in range(value) :
        print(idx)