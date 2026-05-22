def count(reserved,indx):
    global res
    if indx==8:
        res+=1
        return
    for i in range(8):
        if i not in reserved and board[indx][i]!="*":
            s=True
            c=1
            for j in range(len(reserved)-1,-1,-1):
                if abs(i-reserved[j])==c:
                    s=False
                c+=1
            if s:
                count(reserved+[i],indx+1)

board=[]
for i in range(8):
    row=list(map(str,input().strip()))
    board.append(row)
res=0
count([],0)
print(res)