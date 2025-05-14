n,k = map(int,input().split())


def pact(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

np = pact(n)
kp = pact(k)
nkp = pact(n-k)

print(np // (kp*nkp))

# print(np)
# print(kp)
# print(nkp)
