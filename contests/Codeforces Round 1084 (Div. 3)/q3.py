t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input())
    for i in range(1,n):
        if s[i]==s[i-1]:
            s[i]="*"
            s[i-1]="*"
    state=False
    st=[]
    for i in range(0,n):
        if s[i]=="*":
            continue
        if st and s[st[-1]]==s[i]:
            s[st.pop()]="*"
            s[i]="*"
        else:
            st.append(i)
    if len(st)==0:
        state=True
    if state:
        print("YES")
    else:
        print("NO")