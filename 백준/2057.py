def factorial(n):
    if n==0:
        return 1
    else:
        return n*(factorial(n-1))
fact_list=[factorial(i) for i in range(21)]
N=int(input())
if N==0:
    print("NO")
else:
    for i in range(20,-1,-1):
        if N>=fact_list[i]:
            N-=fact_list[i]
    if N==0:
        print("YES")
    else:
        print("NO")
    
#알고리즘은 맞았지만 구현에는 실패