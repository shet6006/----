list=[]
for i in range(9):
    n=int(input())
    list.append(n)
sorted_list=sorted(list, reverse=True)
print(sorted_list[0])
for i in range(9):
    if sorted_list[0]==list[i]:
        print(i+1)