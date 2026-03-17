n = int(input())
arr = list(map(int, input().split()))

best_entrance = 1
best_time = 10**30

for i in range(n):
        if arr[i] <= i:
                cur_time = i
        else:
                rounds = (arr[i] - i + n - 1) // n
                cur_time = i + rounds * n

        if cur_time < best_time:
                best_time = cur_time
                best_entrance = i + 1

print(best_entrance)
