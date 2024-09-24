A = input()
B = input()
print(f'{len(A)} {len(B)}')
print(f'{A+B}')
new_A = B[0] + A[1:]
new_B = A[0] + B[1:]
print(f'{new_A} {new_B}')