#배열A의 가장 작은원소와 배열 B의 가장 큰원소 swap
N, K = map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
sorted_A=sorted(A)
sorted_B=sorted(B,reverse=True)
for i in range(K):
    if sorted_A[i] < sorted_B[i]:
        sorted_A[i] = sorted_B[i]
        #sorted_A[i], sorted_B[i] = sorted_B[i], sorted__A[i]와 같이 쓸 수 있음
    else:
        break
sum=0
for i in range(N):
    sum+=sorted_A[i]
print(sum)