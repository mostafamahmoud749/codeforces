import sys

sys.stdin = open("div7.in", "r")
sys.stdout = open("div7.out", "w")

n = int(input())
prefix_sum = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + int(input())
    prefix_sum[i] %= 7

first_occurrence = [-1] * 7
first_occurrence[0] = 0  
max_length = 0

for i in range(1, n + 1):
    mod_val = prefix_sum[i]
    if first_occurrence[mod_val] == -1:
        first_occurrence[mod_val] = i
    else:
        max_length = max(max_length, i - first_occurrence[mod_val])

print(max_length)