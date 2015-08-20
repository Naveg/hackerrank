def get_moves(chocolates):
    moves_to_zero = 0
    for c in chocolates:
        if c > 0:
            moves_to_zero += c//5
            c = c % 5
            moves_to_zero += c//2
            c = c % 2
            moves_to_zero += c

    min_chocs = min(chocolates)
    chocolates = list(c - min_chocs for c in chocolates)
    moves_to_min = 0
    for c in chocolates:
        if c > 0:
            moves_to_min += c//5
            c = c % 5
            moves_to_min += c//2
            c = c % 2
            moves_to_min += c
    return min(moves_to_zero, moves_to_min)
    

T = int(input())
for t in range(T):
    n = int(input())
    chocolates = list(map(int, input().split()))
    print(get_moves(chocolates))
