length = int(input())
string = input()

two_cnt = string.count('2')
e_cnt = string.count('e')

result = '2' if two_cnt > e_cnt else 'e' if e_cnt > two_cnt else 'yee'
print(result)