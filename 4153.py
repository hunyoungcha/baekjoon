while True:
    x,y,z = map(int,input().split())
    if (x+y+z == 0): break
    

    if ((x**2 + y**2 == z**2) or (y**2 + z**2 == x**2) or (x**2 + z**2 == y**2)):
        print("right")
    else:
        print("wrong")