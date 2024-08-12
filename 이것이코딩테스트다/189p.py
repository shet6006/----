#이진탐색소스코드

# def binary_search(array, target, start,end):
#     if start > end:
#         return None
#     mid = (start+end)//2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     elif array[mid] < target:
#         return binary_search(array, target, mid+1, end)
    
# n, target=list(map(int, input().split()))
# array = list(map(int, input().split()))

# result=binary_search(array, target, 0, n-1)

# if result == None:
#     print("none")
# else:
#     print(result+1)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result==None:
    print("none")
else:
    print(result+1)