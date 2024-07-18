##########틀린 풀이##########
#입력 배열 저장
# list=[]
# while True:
#     line=input()
#     if line == "# 0 0":
#         break
#     list.append(line)
# split=[string.split() for string in list]   
# name=[sublist[0] for sublist in split] 
# age=[int(sublist[1]) for sublist in split]
# weight=[int(sublist[2]) for sublist in split]
# for name,age,weight in zip(name,age,weight): #세개를 한번에 순회
#     if age> 17 or weight >= 80:
#         print(f"{name} Senior")
#     else:
#         print(f"{name} Junior")
##########맞은 풀이##########
while True:
    name, age, weight = input().split()
    if '#' in name:
        break
    if int(age) > 17 or int(weight) >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")