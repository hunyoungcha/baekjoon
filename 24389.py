a = int(input())

bin_a = f'{a & 0xFFFFFFFF:032b}'  # 32비트 유지
bin_a2 = f'{~a +1 & 0xFFFFFFFF:032b}'  # 32비트 유지

cnt=0

for i in range(len(bin_a)):
    if bin_a[i] != bin_a2[i]:
        cnt +=1

print(cnt)