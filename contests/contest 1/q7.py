t=int(input())
for _ in range(t):
    sum=0
    for i in range(0,10):
        row=input()
        for j in range(0,10):
            if row[j]=='X' and i<5 and j<5:
                sum+=min(i,j)+1
            elif row[j]=='X' and i>=5 and j<5:
                sum+=min(9-i,j)+1
            elif row[j]=='X' and i<5 and j>=5:
                sum+=min(i,9-j)+1
            elif row[j]=='X' and i>=5 and j>=5:
                sum+=min(9-i,9-j)+1
    print(sum)