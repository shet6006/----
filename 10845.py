import sys
N=int(sys.stdin.readline())
queue=[]
front=0
rear=0
for i in range(N):
    order = sys.stdin.readline().split()
    if len(order) > 1:
        order[1]=int(order[1])
    if order[0]=='push':
        queue.append(order[1])
        rear=rear+1
    if order[0]=='pop':
        if front < rear:
            print(queue[0])
            queue.pop(0)
            front+=1
        else:
            print(-1)
    if order[0]=='size':
        print(rear-front)
    if order[0]=='front':
        if front < rear:
            print(queue[0])
        else:
            print(-1)
    if order[0]=='back':
        if front < rear:
            print(queue[rear-front-1])
        else:
            print(-1)
    if order[0]=='empty':
        if front==rear:
            print(1)
        else:
            print(0)