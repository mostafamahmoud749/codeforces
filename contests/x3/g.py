import math

t=int(input())
for i in range(t):
    n=int(input())
    s=input()

    freq={}

    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    m=max(freq.values())
    # print(m)
    op=0
    while m <= n//2 :
        op+=1
        m += 1
        n += 1
    print(op)