def marge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        left_half = marge_sort(left_half)
        right_half = marge_sort(right_half)
        return merge(left_half, right_half)

def merge(left, right):
    i = j = 0
    new = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
arr = list(map(int, input().split()))
sorted_arr = marge_sort(arr)
print(sorted_arr)
            
    