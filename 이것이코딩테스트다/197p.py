import sys

N=int(sys.stdin.readline())
input_data = list(map(int, sys.stdin.readline().rstrip().split()))
input_data.sort()
M=int(sys.stdin.readline())
offer_data = list(map(int,sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end -= mid -1
        else:
            start += mid +1
    return None

for i in range(len(offer_data)):
    result = binary_search(input_data, offer_data[i], 0, len(input_data)-1)
    if result == None:
        print('no', end= ' ')
    else:
        print('yes', end = ' ')
