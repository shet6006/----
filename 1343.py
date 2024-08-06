#. 뒤에 x가 네개or두개 연속으로 오는지 보기
#두개면 BB로 바꾸고 네개면 AAAA로
N=input()
lists=[]
count=0
b_count=0
for char in N:
    lists.append(char)
for i in range(len(lists)):
    if lists[i]=='X':
        count+=1
    elif lists[i]=='.':
        count=0
        b_count=0
    if count==2:
        for j in range(2):
            lists[i-j] = 'B'
        count=0
        b_count+=2
    if b_count==4:
        for j in range(4):
            lists[i-j] = 'A'
        count=0
        b_count=0
if 'X' in lists:
    print(-1)
else:
    print(''.join(lists))
