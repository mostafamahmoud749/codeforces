t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ones = s.count('1')
    
    if n % 2 == 1 and ones % 2 == 1:
        print(-1)
    else:
        if ones % 2 == 0:
            indices = [i + 1 for i, ch in enumerate(s) if ch == '1']
        else:
            indices = [i + 1 for i, ch in enumerate(s) if ch == '0']
        
        print(len(indices))
        if indices:
            print(' '.join(map(str, indices)))