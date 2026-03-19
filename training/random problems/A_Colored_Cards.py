db=["Green","Yellow","Blue","Pink"]
t=int(input())
for _ in range(t):
    n=int(input())
    print(db[(n%4)-1])
