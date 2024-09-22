
def binary(arr, target):
    left,right = 0, len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
arr = [10, 20, 30, 40, 50]
sorted_index=binary(arr, 10)
print(sorted_index)



