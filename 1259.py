while True:
    n=input()

    if n =='0' : break

    sw = True

    for i in range(len(n)//2):
        if n[i] != n[-i-1] :
            sw = False

    if (sw):
        print("yes")
    else:
        print("no")