n = int(input())

names  = []
for _ in range(n):
    name = input()

    if len(name) ==3 :
        names.append(name)

print(sorted(names)[0])