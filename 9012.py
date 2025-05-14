n = int(input())

for i in range(n):
    string = input()

    cnt = 0
    for i in string:
        if i == "(" :
            cnt +=1
        elif i == ")":
            cnt -= 1

        if cnt < 0 :
            break
    print("YES" if cnt == 0 else "NO")