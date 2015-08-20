from collections import deque

def get_profit2(prices):
    max_right_of = deque()
    max_so_far = -1
    for p in prices[::-1]:
        max_right_of.appendleft(max_so_far if max_so_far > p else -1)
        max_so_far = max(max_so_far, p)

    held_shares = 0
    held_cost = 0
    profit = 0
    for i,p in enumerate(prices):
        if max_right_of[i] > -1:
            held_shares += 1
            held_cost += p
        else:
            profit += p * held_shares - held_cost
            held_shares = 0
            held_cost = 0
    return profit

T = int(input())
for t in range(T):
    n = int(input())
    prices = list(map(int, input().split()))
    print(get_profit2(prices))
