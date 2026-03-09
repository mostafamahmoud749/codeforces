n=int(input())
errors=list(map(int,input().split()))
errors.sort()

for _ in range(2):
    new_errors=list(map(int,input().split()))
    new_errors.sort()
    for i in range(len(new_errors)):
        if new_errors[i]!=errors[i]:
            print(errors[i])
            break
    else:
        print(errors[-1])
    errors=new_errors
