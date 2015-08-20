import sys
sys.setrecursionlimit(10000)

def parse(n):
    tree = dict()
    for i in range(1, n+1):
        tree[i] = tuple(map(int, input().split()))
    return tree

def inorder(tree, root):
    if root == -1:
        return []
    left,right = tree[root]
    return inorder(tree, left) + [root] + inorder(tree, right)

def doswap(tree, root, swaplvl):
    currnodes = [root]
    currlvl = 1

    while currnodes:
        if currlvl % swaplvl == 0:
            for node in currnodes:
                l,r = tree[node]
                tree[node] = (r,l)

        nextnodes = []
        for node in currnodes:
            l,r = tree[node]
            if l != -1:
                nextnodes.append(l)
            if r != -1:
                nextnodes.append(r)
        currnodes = nextnodes
        currlvl += 1

n = int(input())
tree = parse(n)
t = int(input())
for i in range(t):
    doswap(tree, 1, int(input()))
    print(' '.join(map(str, inorder(tree, 1))))
