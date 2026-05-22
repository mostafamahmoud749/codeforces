def fib(n):
    if n<2:
        return 1
    v=fib(n-1)+fib(n-2)
    a.add(v)
    return v

n=int(input())
a=set()
a.add(1)
fib(15)
res=[]
for i in range(n):
    if i+1 in a:
        res.append("O")
    else:
        res.append("o")
print("".join(res))