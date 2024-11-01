fin_cmd = ['#','0','0']

while True:
    a,b,c = map(str,input().split())
    if [a,b,c] == fin_cmd:
        break
    
    if int(b) > 17 or int(c) >=80 : print(f'{a} Senior')
    else: print(f'{a} Junior')     