# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# if sorted(A) == sorted(B):
#     print("yes")
# else:
#     print("no")

A = [1, 2, 3, 4, 5]
mid = len(A)//2
left = A[:mid]
right = A[mid+1:]
A = left+right
print(A)

