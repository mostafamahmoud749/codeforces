for _ in range(int(input())):
    l,r = map(int, input().split())
    res = -1
    ans = 0
    y = 0
    for i in range(63,0,-1):
        c = 1 << i
        # print(c)
        if r&c and not(l&c):
            x = y | (c-1)
            # print(bin(x)[2:])
            if res == -1 or x.bit_count() >= res.bit_count():
                res = x
                # res = min(res,x)
            
        if r&c and l&c:
            y |= c
    
    print(res if res != -1 else l)

# print(int('10111',base=2))