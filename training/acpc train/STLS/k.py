t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for i in range(n):
        key = a[i] - i
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1
    res = 0
    for count in freq.values():
        res += count * (count - 1) // 2
    print(res)