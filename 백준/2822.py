score=[]
index=[]
sum=0
for i in range(8):
    score.append(int(input()))

for i in range(5):
    max_score=score.index(max(score))
    sum += max(score)
    index.append(max_score+1)
    score[max_score] = -1
index.sort()
print(sum)
for x in index:
    print(x, end= ' ')