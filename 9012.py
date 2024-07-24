N=int(input())
for i in range(N):
    ps_list=[]
    ps=input()
    for char in ps:
        if char == '(':
            ps_list.append(char)
        if char == ')':
            if len(ps_list)>0:
                if ps_list[-1] == '(':
                    ps_list.pop()
            else:
                ps_list.append(char)


    if len(ps_list)==0:
        print('YES')
    else:
        print('NO')
