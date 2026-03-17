import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])
x = int(data[1])
a = list(map(int, data[2:2+n]))

prefix_sum = 0
count = {0: 1}
result = 0

for num in a:
    prefix_sum += num
    target = prefix_sum - x
    if target in count:
        result += count[target]
    
    if prefix_sum in count:
        count[prefix_sum] += 1
    else:
        count[prefix_sum] = 1

print(result)