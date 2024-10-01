# def buuble(arr):
#     N = len(arr)
#     for i in range(N):
#         swapped = False
#         for j in range(0, N-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] =arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# arr= list(map(int,input().split()))
# sorted = buuble(arr)
# print(sorted)

def selection(arr):
    N = len(arr)
    for i in range(N-1):
        min = i
        for j in range(i+1, N):
            if arr[j] < arr[min]:
                min = j
                arr[i], arr[min] = arr[min], arr[i] 
    return arr
arr = [24, 41, 33, 42, 17]
srt = selection(arr)
print(srt)
    