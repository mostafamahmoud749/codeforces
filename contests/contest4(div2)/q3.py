
t = int(input())
for _ in range(t):
    s, m = map(int, input().split())
    low = m & -m
    if s % low != 0:
        print(-1)
        continue

    lo, hi = 1, s
    ans = s
    while lo <= hi:
        mid = (lo + hi) // 2
        L = 0
        R = 0
        ok = True
        for i in range(61):          
            s_bit = (s >> i) & 1
            allowed = (m >> i) & 1
            if allowed:
                newL = (L - s_bit + 1) // 2          

                p = (s_bit ^ (R & 1))
                if p == 0:
                    c_max = mid if (mid % 2 == 0) else mid - 1
                else:
                    c_max = mid if (mid % 2 == 1) else mid - 1
                newR = (R - s_bit + c_max) // 2

                L, R = newL, newR
            else:
                parity = s_bit
                r_min = L if (L & 1) == parity else L + 1
                if r_min > R:
                    ok = False
                    break
                r_max = R if (R & 1) == parity else R - 1
                if r_max < r_min:
                    ok = False
                    break
                newL = (r_min - s_bit) // 2
                newR = (r_max - s_bit) // 2
                L, R = newL, newR

            if L > R:
                ok = False
                break

        if ok and L <= 0 <= R:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)