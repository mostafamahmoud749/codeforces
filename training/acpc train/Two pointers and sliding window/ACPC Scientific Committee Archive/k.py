import math
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    v=math.gcd(x,y)
    print(v-1)