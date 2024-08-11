n=input()
for i in range(1,int(n)+1): #i는 1부터 n+1까지 반복
    # print('*' * i) #왼쪽으로 정렬
    print(' '*(int(n)-i) + '*'*i) #공백개수만큼 찍고, 그 뒤로 별 찍기