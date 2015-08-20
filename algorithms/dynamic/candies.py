def get_candies(ratings):
    if len(ratings) == 1:
        return 1
    candies = list(1 for r in ratings)
    minima = list()

    for i,r in enumerate(ratings):
        prevr = ratings[i-1] if i > 0 else 10**6
        nextr = ratings[i+1] if i < len(ratings)-1 else 10**6
        if r <= prevr and r <= nextr:
            minima.append(i)

    for minimum in minima:
        curr = 1
        i = minimum
        while i > 0 and ratings[i-1] > ratings[i]:
            candies[i-1] = max(candies[i-1], candies[i] + 1)
            i -= 1
        i = minimum
        while i < len(ratings) - 1 and ratings[i+1] > ratings[i]:
            candies[i+1] = max(candies[i+1], candies[i] + 1)
            i += 1
    return sum(candies)

n = int(input())
ratings = list()
for i in range(n):
    ratings.append(int(input()))

print(get_candies(ratings))
