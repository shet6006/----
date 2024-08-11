# N,K=map(int,input().split())
# print(N,K)
# count=0
# while N!=1:
#     if N%K==0:
#         N=N//K
#         count+=1
#     else:
#         N=N-1
#         count+=1
# print(count)

N,K=map(int,input().split())
count=0
while True:
    target=(N//K)*K
    count+=(N-target)
    if N<K:
        break
    count+=1
    N//=K
count+=(N-1)
