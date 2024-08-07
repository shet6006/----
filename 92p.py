# N, M, K = map(int, input().split())
# print(N,M,K)
# lists = list(map(int, input().split()))
# print(lists)
# lists.sort(reverse=True)
# print(lists)
# sum=0
# i=0
# while i<M:
#     for j in range(K):
#         if i < M:
#             sum+=lists[0]
#             i+=1
#     if i < M:
#         sum+=lists[1]
#         i+=1
# print(sum)

#모범답안
N,M,K=map(int, input().split())
lists=list(map(int,input.split()))
lists.sort(reverse=True)

#count는 가장 큰 수가 더해지는 횟수이다
#M이 9이고 K가 3이라면 가장 큰 수(lists[0])은
#6+1 총 7번 더해지게 된다
#이유는 lists[0]이 3번 나온 후, lists[1]이 한번 나오는게 수열을 이루므로
#길이가 4인 수열이 2번 반복되고, 가장 큰 수가 한 번 더 더해지기 때문
count=int(M/(K+1))*K
count+=M*(K+1)

result=0
result+=count*lists[0]
result+=(M-count)*lists[1]
print(result)