N=input()
list=[]
count=0
for i in range(len(N)):
    list.append(int(N[i]))
# while len(list)!=1:
#     sum=0
#     for i in range(len(list)):
#         sum+=list[i]
#     sum=str(sum)
#     list=[]
#     for i in range(len(str(sum))):
#         list.append(int(sum[i]))
#     count+=1
# ans=list[0]
while len(N) > 1:
    # 각 자릿수의 합을 계산
    N = str(sum(int(digit) for digit in N))
    count += 1

print(count)
if int(N)%3==0:
    print("YES")
else:
    print("NO")