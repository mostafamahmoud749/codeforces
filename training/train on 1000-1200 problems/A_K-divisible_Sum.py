import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = (n + k - 1) // k  
    x = (m * k + n - 1) // n 
    print(x)