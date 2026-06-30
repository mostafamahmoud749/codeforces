n=int(input())
a=list(map(int,input().split()))
m=max(a)

freq=[0]*m
for i in a:
    freq[i-1]+=1

dp=[0]*m
dp[-1]=m*freq[-1]

for i in range(m-2,-1,-1):
    ch1=dp[i+1]
    ch2=(i+1)*freq[i]
    if i<len(dp)-2:
        ch2+=dp[i+2]
    dp[i]=max(ch1,ch2)

# print(a)
# print(dp)
# print(freq)
print(dp[0])