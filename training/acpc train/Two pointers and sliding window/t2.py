n,x=map(int,input().split())
a=list(map(int,input().split()))

if n<3:
    print("IMPOSSIBLE")
else:
    arr = [(val,idx+1) for idx,val in enumerate(a)]
    arr.sort()
    for k in range(2,n):
        v=x-arr[k][0]
        i=0
        j=k-1
        while i<j:
            if arr[i][0]+arr[j][0]==v:
                print(arr[i][1],arr[j][1],arr[k][1])
                exit()
            elif arr[i][0]+arr[j][0]<v:
                i+=1
            else:
                j-=1
    print("IMPOSSIBLE")