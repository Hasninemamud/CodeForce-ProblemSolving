seat_per_row = 4
seat_num = int(input())

# Calculate the row and column
row = seat_num // seat_per_row  # Get the row
col_num = seat_num % seat_per_row  # Get the column (starting from 0)

print(f"Row: {row}, Column: {col_num}")
