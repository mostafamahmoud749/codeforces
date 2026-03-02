t=int(input())
y="codeforces"
for i in range(t):
    n=input()
    count=0
    for k in range(10):
        if y[k]!=n[k]:
            count+=1
    print(count)
