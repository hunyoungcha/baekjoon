n = int(input())

s = set()

for i in range(n):
    s.add(input())

l = list(s)
sorted_l = sorted(l, key=lambda x:(len(x),x))

for i in sorted_l:
    print(i)