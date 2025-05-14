n,m = map(int,input().split())

a,b=min(n,m), max(n,m)

while b:
    a,b = b, a%b

print(a)
print(n*m //a)