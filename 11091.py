num = int(input())

for _ in range(num):
    alpha_dict = {'a':0, 'b':0, 'c':0,'d':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0 }

    string = input().lower()

    for str in string:
        if str in alpha_dict:
            alpha_dict[str] = 1

    zero_value = [key for key,value in alpha_dict.items() if value == 0]

    if zero_value != []:
        print("missing", ''.join(zero_value))
    else:
        print('pangram')