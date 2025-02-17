n = int(input())

str_list = []
for i in range(n):
    tmp = input().split()
    str_list.append(tmp)

for i in str_list:
    print(' '.join(i[2:]), end=' ')
    print(' '.join(i[:2])) 