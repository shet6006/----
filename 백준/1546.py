sum=0
N=int(input())
score=list(map(int, input().split()))
max_score=max(score)
for i in range(N):
    score[i]=score[i]/max_score*100
    sum+=score[i]
print(sum/N)