from collections import deque

def get_sum(values, k):
    values = sorted(values)
    can_create = set([0])
    q = deque([0])
    while q:
        i = q.pop()
        if i > 10*k:
            break
        for val in values:
            s = i + val
            if s not in can_create:
                can_create.add(s)
                q.appendleft(s)
    for i in range(k, 0, -1):
        if i in can_create:
            return i
    return 0

T = int(input())
for t in range(T):
    n,k = list(map(int, input().split()))
    values = list(map(int, input().split()))
    print(get_sum(values, k))
