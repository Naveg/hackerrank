ways = dict()
ways[0] = 1
for n in range(1, 41):
    ways[n] = ways[n-1] + (ways[n-4] if n >= 4 else 0)
 
def rwh_primes(n):
    # adapted from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    if n <= 2:
        return []
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

T = int(input())
for t in range(T):
    n = int(input())
    print(len(rwh_primes(ways[n] + 1)))
