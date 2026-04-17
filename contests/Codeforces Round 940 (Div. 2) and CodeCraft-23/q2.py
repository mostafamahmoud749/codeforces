t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n == 1:
        print(k)
    else:
        b=k.bit_length()-1
        num1=(2**b)-1
        num2=k-num1
        print(num1,num2,*[0]*(n-2))