a,b=map(int,input().split())
used_candles=0
hours=0
while a :
    used_candles+=1
    a-=1
    hours+=1
    if used_candles==b:
        a+=1
        used_candles=0
print(hours)

