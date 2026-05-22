def sort(n,a):
    sa=a.copy()
    sa.sort()
    if a==sa:
        return n
    ch1=sort(n//2,a[:n//2])
    ch2=sort(n//2,a[n//2:])
    return max(ch1,ch2)

n=int(input())
a=list(map(int,input().split()))
print(sort(n,a))