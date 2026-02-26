t = int(input().strip())

for _ in range(t):
    s = input().strip()
    digits = [int(ch) for ch in s]
    total = sum(digits)

    if total <= 9:
        print("0")
        continue

    need = total - 9               
    reductions = []

    for i, d in enumerate(digits):
        if i == 0:                 
            reductions.append(d - 1)
        else:                   
            reductions.append(d)

    
    reductions.sort(reverse=True)

    cur = 0
    cnt = 0
    for r in reductions:
        cur += r
        cnt += 1
        if cur >= need:
            break

    print(str(cnt))

