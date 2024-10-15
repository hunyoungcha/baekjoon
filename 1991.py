#트리 순회

length = int(input())

tree = {}

for _ in range(length):
    value, left, right = map(str, input().split())
    tree[value] = left, right


#전위 순회
def preorder(v): 
    if v != ".":
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])

#중위 순회
def inorder(v):
    if v != ".":
        inorder(tree[v][0])
        print(v, end="")
        inorder(tree[v][1])

#후위 순회
def postorder(v):
    if v != ".":
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")