def calc(s,cl):
    if len(s)==1:
        if cl==s[0]:
            return 0
        else:
            return 1
    ch1=((len(s)//2)-(s[:len(s)//2].count(cl)))+calc(s[len(s)//2:],chr(ord(cl)+1))
    ch2=((len(s)//2)-(s[len(s)//2:].count(cl)))+calc(s[:len(s)//2],chr(ord(cl)+1))
    return min(ch1,ch2)

t=int(input())
for _ in range(t):
    n=int(input())
    s=list(input().strip())
    res=calc(s,"a")
    print(res)