import math

pwrs = set(str(2**x) for x in range(801))

def count_pwrs2(s):
    count = 0
    for pwr in pwrs:
        start = s.find(pwr, 0) + 1
        while start > 0:
            count += 1
            start = s.find(pwr, start) + 1
    return count

T = int(input())
for t in range(T):
    s = input().strip()
    print(count_pwrs2(s))
