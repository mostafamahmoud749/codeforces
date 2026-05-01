n = input()
count = [0] * 2019
count[0] = 1
current = 0
power = 1
ans = 0

for i in range(len(n)-1, -1, -1):
    current = (int(n[i]) * power + current) % 2019
    power = (power * 10) % 2019
    ans += count[current]
    count[current] += 1

print(ans)