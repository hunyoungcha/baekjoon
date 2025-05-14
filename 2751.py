import sys
input_ = sys.stdin.readline

n = int(input_())

l = []
for i in range(n):
    l.append(int(input_()))
l.sort()

[print(i) for i in l]