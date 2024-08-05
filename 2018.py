N=int(input())
start,end=1,1
count=0
sums=1
while end != N:
    if sums<N:
        end+=1
        sums+=end
    elif sums>N:
        sums-=start
        start+=1
    else:
        end+=1
        sums+=end
        count+=1
print(count+1)