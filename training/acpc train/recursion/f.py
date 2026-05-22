
def create(crn,numbers):
    if len(crn)==ln:
        r="".join(crn)
        if int(r)>=int(n):
            p.append(int(r))
        return
    seen=set()
    for i in range(len(numbers)):
        if numbers[i] in seen:
            continue
        seen.add(numbers[i])
        nn=crn.copy()
        nns=numbers.copy()
        nn.append(numbers[i])
        nns.pop(i)
        create(nn,nns)

n=input()
ln=len(n)
numbers=[]
p=[]

if ln%2!=0:
    ln+=1
    print(((ln//2)*"4")+((ln//2)*"7"))
    exit()

p.append(int((((ln+2)//2)*"4")+(((ln+2)//2)*"7")))

for i in range(ln):
    if i<ln//2:
        numbers.append("4")
    else:
        numbers.append("7")

create([],numbers)

print(min(p))
