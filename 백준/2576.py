list=[]
total=0
for i in range(7):
    number=int(input())
    if number%2==1:
        list.append(number)
        total+=number
if list:
    print(total)
    print(min(list)) #파이썬의 min함수
else:
    print(-1)