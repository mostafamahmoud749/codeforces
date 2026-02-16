k, w = map(int, input().split())
planks = list(map(int, input().split()))

start = sum(planks[:w])
minsum = start
index = 0

for i in range(1, k - w + 1):
    start = start - planks[i - 1] + planks[i + w - 1]
    if start < minsum:
        minsum = start
        index = i

print(index + 1)