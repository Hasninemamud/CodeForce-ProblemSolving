# # A, B = map(int,input().split())
# # S = input()
# # if S[A] == '-' and S[:A].isdigit() and S[A+1:].isdigit():
# #     print("Yes")
# # else:
# #     print("No")

# # # # 2 6 9 - 6 6 5
# # # # 0 1 2 3 4 5 6

# # 5 = 5-1 + 4-2 + 2 

# def fib(N):
#     # Base cases
#     if N == 1:
#         return 0
#     elif N == 2:
#         return 1
    
#     # Initialize the first two Fibonacci numbers
#     a, b = 0, 1
    
#     # Calculate Fibonacci numbers iteratively up to N
#     for i in range(3, N + 1):
#         a, b = b, a + b
    
#     return b

# # Input reading
# N = int(input())  # Read the number N

# # Output the Fibonacci number for N
# print(fib(N))
# # fib(n) = fib(n-1) + fib(n-2)
#         # = 7 - 1 + 6 - 2 + 4 - 3 + 1

def marge_sort(arr):
    if len(arr) <= 1:
        return 1
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]  
        right_half = arr[mid:]

        left_half = marge_sort(left_half)
        right_half = marge_sort(right_half)
        return merge(left_half,right_half)

def merge(left, right):
    new = []
    i = j = 0
    while i < left[i] and j < right[j]:
        if left[i] < right[j]:
           new.append(left[i])
           i += 1
        else:
           new.append(right[j])
           j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

arr = list(map(int,input().split()))
sorted = marge_sort(arr)
print(sorted)

