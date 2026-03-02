n=int(input())
for i in range(n):
    y=input()
    if len(y)==1:
        print(y)
    else:
        print(int(y[0])+int(y[1]))