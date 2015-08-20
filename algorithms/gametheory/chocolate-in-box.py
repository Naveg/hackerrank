import functools
n = int(input())
boxes = list(map(int, input().split()))

nimsum = functools.reduce(lambda x,y: x^y, boxes)
newboxes = list(map(lambda x: x^nimsum, boxes))
print(sum(list(1 for i in range(len(boxes)) if newboxes[i] < boxes[i])))
