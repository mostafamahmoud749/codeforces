t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=sorted(map(int,input().split()))

    cur_indx=0
    last_el=a[0]
    last_el_c=1
    new_a=[[] for _ in range(n)]

    for i in range(1,n):
        if a[i]==last_el:
            last_el_c+=1
        elif a[i]==last_el+1 and len(new_a[cur_indx])<k:
            new_a[cur_indx].append(last_el_c)
            last_el=a[i]
            last_el_c=1
        elif a[i]==last_el+1 and len(new_a[cur_indx])>=k:
            cur_indx+=1
            new_a[cur_indx]=new_a[cur_indx-1][:]
            new_a[cur_indx].pop(0)
            new_a[cur_indx].append(last_el_c)
            last_el=a[i]
            last_el_c=1
        else:
            if len(new_a[cur_indx])<k:
                new_a[cur_indx].append(last_el_c)
            else:
                cur_indx+=1
                new_a[cur_indx]=new_a[cur_indx-1][:]
                new_a[cur_indx].pop(0)
                new_a[cur_indx].append(last_el_c)
            cur_indx+=1
            new_a[cur_indx]=[]
            last_el_c=1
            last_el=a[i]
    if len(new_a[cur_indx])<k:
        new_a[cur_indx].append(last_el_c)
    else:
        cur_indx+=1
        new_a[cur_indx]=new_a[cur_indx-1][:]
        new_a[cur_indx].pop(0)
        new_a[cur_indx].append(last_el_c)
    
    max_sum=0
    for i in new_a:
        if len(i)==0:
            break
        max_sum=max(sum(i),max_sum)
    print(max_sum)
