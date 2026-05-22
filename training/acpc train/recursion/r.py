def count(reserved,indx):
    global res
    if indx==n:
        board=[]
        for i in range(n):
            row=["."]*n
            row[reserved[i]]="Q"
            board.append("".join(row))
        res.append(board)
        return
    for i in range(n):
        if i not in reserved:
            s=True
            c=1
            for j in range(len(reserved)-1,-1,-1):
                if abs(i-reserved[j])==c:
                    s=False
                    break
                c+=1
            if s:
                count(reserved+[i],indx+1)

n=int(input())
res=[]
count([],0)
for i in range(len(res)):
    for row in res[i]:
        print(row)
    print()
