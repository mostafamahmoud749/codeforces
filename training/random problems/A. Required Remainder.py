t=int(input())
for i in range(t):
    x,y,n=map(int,input().split())
    q = (n-y)//x 
    k = x*q+y
    print(k)
        