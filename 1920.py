import sys

input_ = sys.stdin.readline

n = int(input_())
nn = map(int,input().split())
nd = {key:0 for key in nn}

m = int(input_())
mn = map(int,input_().split())

for i in mn :
    print("1" if i in nd else '0')