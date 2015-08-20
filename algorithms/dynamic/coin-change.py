n, m = list(map(int, input().split()))
coins = list(map(int, input().split()))

known_ways = dict()

def get_ways(total, coins, last_coin):
    if (total, last_coin) in known_ways:
        return known_ways[(total, last_coin)]
    if total < 0:
        return 0
    if last_coin < 0:
        return 0
    if total == 0:
        return 1

    ways = get_ways(total, coins, last_coin - 1) + get_ways(total - coins[last_coin], coins, last_coin)
    known_ways[(total, last_coin)] = ways
    return ways

print(get_ways(n, coins, len(coins) - 1))
