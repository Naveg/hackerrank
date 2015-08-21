from collections import defaultdict

def substrings(s):
    subs = list()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs.append(s[i:j])
    return subs

def nCk(n, k):
    nck = 1
    for i in range(1, k + 1):
        nck *= (n - k + i) / i
    return int(nck)

def anagram_pairs(subs):
    sortedsubs = list(str(sorted(s)) for s in subs)
    counts = defaultdict(int)
    for s in sortedsubs:
        counts[s] += 1
    pairs = 0
    for k,v in counts.items():
        pairs += nCk(v, 2)
    return pairs

T = int(input())
for t in range(T):
    s = input().strip()
    print(anagram_pairs(substrings(s)))
