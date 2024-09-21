n = str(input())
rev = n[::-1]
rmv_zero = rev.lstrip('0')
print(rmv_zero)
if n == rmv_zero:
    print("Yes")
else:
    print('No')