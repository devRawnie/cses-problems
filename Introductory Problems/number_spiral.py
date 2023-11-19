"""
1  2  9  10 25 26
4  3  8  11 24 27
5  6  7  12 23 28
16 15 14 13 22 29
17 18 19 20 21 30
36 35 34 33 32 31


1
2 3 4
5 6 7 8 9
10 11 12 13 14 15

row_number
 - odd
   - first_number_in_row: (row_number - 1)**2 + 1
   - order: increasing 
 - even:
   - first_number_in_row: row_number**2
   - order: decreasing

col_number
 - odd
   - first_number_in_col: col_number**2
   - order: decreasing
 - even
   - first_number_in_col: (col_number-1)**2 + 1
   - order: increasing

if row_number, col_number = 1 -> return 1

n = max(row_number, col_number)


"""