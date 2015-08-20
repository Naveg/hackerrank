import sys
from collections import deque, defaultdict
sys.setrecursionlimit(100000)

class Node():
    def __init__(self, value):
        self.value = value
        self.children = list()

n = int(input())
vals = list(map(int, input().split()))
nodes = list(map(Node, vals))

edges = defaultdict(set)
for i in range(1, n):
    i,j = list(map(int, input().split()))
    edges[i-1].add(j-1)
    edges[j-1].add(i-1)

q = deque([0])
intree = set()
while q:
    i = q.pop()
    if i not in intree:
        intree.add(i)
        node = nodes[i]
        for j in edges[i]:
            if j not in intree:
                q.appendleft(j)
                node.children.append(nodes[j])

def build_sum_tree(root):
    tot = root.value
    children = list(map(build_sum_tree, root.children))
    tot += sum(list(c.value for c in children))
    node = Node(tot)
    node.children.extend(children)
    return node

def min_diff(root):
    ft = root.value
    mindiff = abs(ft)
    q = deque(root.children)
    while q:
        node = q.pop()
        diff = abs(ft - 2 * node.value)
        if diff < mindiff:
            mindiff = diff
        q.extendleft(node.children)
    return mindiff

print(min_diff(build_sum_tree(nodes[0])))
