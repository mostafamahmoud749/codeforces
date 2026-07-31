from math import ceil
for i in range(int(input())):
    l , r = input().split()

    n1 = 0
    for i in l :
        n1 += int(i)
    n2 = 0
    for i in r :
        n2 += int(i)
    
    tot = int(r) - (int(l)) + 1

    if l == r :
        if n1 % 2 == 0 :
            print(0)
        else:
            print(1)
    else:
        if n1 % 2 == 0 :
            tot -= 1
        if n2 % 2 == 0 :
            tot -= 1
        print(ceil(tot/2))        
