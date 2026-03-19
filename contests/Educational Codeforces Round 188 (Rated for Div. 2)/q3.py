
import math

t=int(input())
for _ in range(t):
    a,b,c,m=map(int,input().split())
    lcm_ab = math.lcm(a, b)
    lcm_bc = math.lcm(b, c)
    lcm_ac = math.lcm(a, c)
    lcm_abc = math.lcm(lcm_ab, c)
        
    n_a = m // a
    n_b = m // b
    n_c = m // c
        
    n_ab = m // lcm_ab
    n_bc = m // lcm_bc
    n_ac = m // lcm_ac
    n_abc = m // lcm_abc
        
    ans_a = 6 * n_a - 3 * n_ab - 3 * n_ac + 2 * n_abc
    ans_b = 6 * n_b - 3 * n_ab - 3 * n_bc + 2 * n_abc
    ans_c = 6 * n_c - 3 * n_ac - 3 * n_bc + 2 * n_abc
    print(ans_a,ans_b,ans_c)