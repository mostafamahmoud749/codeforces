t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    max_e=0
    max_e_c=1
    for i in range(n):
        if a[i]>max_e:
            max_e=a[i]
            max_e_c=1
        elif a[i]==max_e:
            max_e_c+=1
    print(max_e_c)
