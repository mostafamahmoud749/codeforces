t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    res=0
    alice=1
    bob=1
    i=0
    j=0
    salice=set()
    sbob=set()
    while i<n:
        if a[i]==b[i]==alice==bob:
            alice+=1
            bob+=1
        elif a[i]==alice and b[i]!=bob:
            while a[j]-1==len(salice):
                sbob.remove(b[j])
                salice.remove(b[j])
                j+=1
        elif a[i]!=alice and b[i]==bob:
            while b[i]!=sbob:
                sbob.remove(b[j])
                salice.remove(b[j])
                j+=1
        i+=1
        res+=i-j
    print(res)