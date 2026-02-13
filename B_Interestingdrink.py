def binarySearch(arr, l, r, x):
    res = -1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] <= x:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res
    

s=int(input())
b=list(map(int,input().split()))
q=int(input())
b.sort()
for _ in range(q):
    c = int(input())
    res = binarySearch(b, 0, s-1, c)
    print(res+1 )

