
def point_along_direction(p, target, length):
    direction = target - p
    dist = abs(direction)
    if dist < 1e-9:
        return p
    unit_dir = direction / dist
    return p + unit_dir * length

t1=int(input())
for _ in range(t1):
    r,n=map(int,input().split())

    c1=r+r*1j

    d1=abs(c1)+r
    d2=abs(point_along_direction(c1,0+0j,r))

    per=d2/d1

    r2=r*(per**n)

    print(f"{r2:.6f}")


