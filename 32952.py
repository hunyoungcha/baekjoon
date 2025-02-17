r, k, m = map(int, input().split())

# 몇 번의 반감기가 발생했는지 계산
num_halvings = m // k

# r을 반감기가 발생한 횟수만큼 2로 나누기
for _ in range(num_halvings):
    r //= 2
    if r == 0:
        break

print(r)
