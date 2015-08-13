from collections import defaultdict
import heapq

EDGE_WEIGHT = 6

def parse_case():
    nv, ne = list(map(int, input().split()))
    edges = list()
    for e in range(ne):
        edges.append(list(map(int, input().split())))
    return Graph(nv, edges), int(input())

class Graph:
    def __init__(self, n, edges):
        self.n = n
        neighbours = defaultdict(set)
        for x,y in edges:
            neighbours[x].add(y)
            neighbours[y].add(x)
        self.neighbours = neighbours

    def get_neighbours(self, x):
        return self.neighbours[x]

    def get_n(self):
        return self.n

def short_dists(g, s):
    '''Returns a dictionary of vertex:distance pairs'''
    dists = defaultdict(lambda: -1)
    dists[s] = 0

    visited = set()

    tovisit = []
    heapq.heappush(tovisit, (dists[s], s))

    while tovisit:
        _, v = heapq.heappop(tovisit)
        distv = dists[v]
        if v in visited:
            continue

        for n in g.get_neighbours(v):
            if dists[n] == -1 or distv + EDGE_WEIGHT < dists[n]:
                dists[n] = distv + EDGE_WEIGHT
            heapq.heappush(tovisit, (dists[n], n))
        visited.add(v)

    return dists

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        g,s = parse_case()
        dists = short_dists(g, s)
        print(' '.join(list(str(dists[v]) for v in range(1, g.get_n() + 1) if v != s)))
