N = list(map(int, input().split()))
print(N)

# for i in range(N[0]): #input :4, 1 2 3 4
#     print(i)
i=1
while i==N[0]:
    print(i)
    i+=1
            
# 1~4까지 중복없이 2개
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3
# 1~4까지 중복없이 4개
# 1 2 3 4
# N[0]이하의 수를 M개씩 조합
# 1~4에서 4개 고른다면
# M-i번 반복