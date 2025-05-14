alp = " abcdefghijklmnopqrstuvwxyz"

n = int(input())
string = input()

result = 0

for i,v in enumerate(string):
    result += 31**i * alp.index(v)

print(result % 1234567891)