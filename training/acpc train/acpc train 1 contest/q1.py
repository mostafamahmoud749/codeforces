t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a+c==b+c :
        if c%2!=0:
            print("First")
        else:
            print("Second")
    elif a+c>b+c:
        print("First")
    else:
        print("Second")
