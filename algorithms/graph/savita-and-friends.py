from collections import defaultdict
import heapq

def parse_case():
    nv, ne, k = list(map(int, input().split()))
    edges = list()
    a,b,r = [0,0,0]
    for e in range(ne):
        edge = list(map(int, input().split()))
        if e == k-1:
            a,b,r = edge
        else:
            edges.append(edge)
    return Graph(nv, edges),a,b,r

class Graph:
    def __init__(self, n, edges):
        self.n = n
        neighbours = defaultdict(set)
        for x,y,r in edges:
            neighbours[x].add((y,r))
            neighbours[y].add((x, r))
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

        for n,r in g.get_neighbours(v):
            if dists[n] == -1 or distv + r < dists[n]:
                dists[n] = distv + r
            heapq.heappush(tovisit, (dists[n], n))
        visited.add(v)

    return dists

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        g,a,b,r = parse_case()
        distsa = short_dists(g, a)
        distsb = short_dists(g, b)
        if distsa[b] > r:
            distsa[b] = -1
        if distsb[a] > r:
            distsb[a] = -1
        maxa = -1
        maxb = -1
        thrua = list()
        thrub = list()
        for n in range(1, g.get_n() + 1):
            if distsa[n] == -1:
                maxb = max(maxb, distsb[n])
            elif distsb[n] == -1:
                maxa = max(maxa, distsa[n])
            else:
                thrub.append(distsb[n])
                thrua.append(distsa[n])
        maxta = max(thrua) if thrua else 0
        maxtb = max(thrub) if thrub else 0
        if (maxtb - maxb) <= (maxta - maxa):
            maxb = maxtb
        else:
            maxa = maxta
        diff = abs(maxa - maxb)
        if maxa == -1:
            p = r
        elif maxb == -1:
            p = 0
        elif maxa <= maxb:
            p = min(r, (r + diff) / 2)
        else:
            p = max(0, r - (r + diff) / 2)
        print('%.5f %.5f' % (p, max(maxa + p if maxa > -1 else 0, maxb + r - p if maxb > -1 else 0)))
