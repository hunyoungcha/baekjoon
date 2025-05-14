import sys
input_ = sys.stdin.readline

while True:
    string = input_()
    if string[0] == '.' : break

    stack = []
    answer = "yes"

    for s in string:
        if s == "(" or s=="[":
            stack.append(s)
        elif s == ")" :
            if not stack or stack.pop() != "(":
                answer = "no"   
                break
        elif s == "]":
            if not stack or stack.pop() != "[":
                answer = "no"
                break
    
    if stack : answer ="no"

    print(answer)