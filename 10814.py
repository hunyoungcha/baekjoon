import sys
inp = sys.stdin.readline

n= int(inp())

l = []

for i in range(n):
    tmp = inp().split() + [i]
    l.append(tmp)

sorted_l = sorted(l, key=lambda x:(int(x[0]), x[2]))
[print(f"{value[0]} {value[1]}") for value in sorted_l]