test_col = False
test_row = False
board = []
for i in range(1, 10):
 play_val = input("Enter your play: ")
 board.append(list(play_val))
for entries in board:
  print(entries)
for col in range(0, 9):
  col_check = []
  col_total = 0
  for row in range(0, 9):
    col_check.append(board[row][col])
  for element in col_check:
    col_total += int(element)
  if col_total == 45:
    test_col = True
    continue
  else:
    test_col = False
    print("No")
    print("Error in column", col+1)
    break
for row in range(0, 9):
  row_check = []
  row_total = 0
  for col in range(0, 9):
    row_check.append(board[row][col])
  for element in row_check:
    row_total += int(element)
  if row_total == 45:
    test_row = True
    continue
  else:
    test_row = False
    print("No")
    print("Error in row", row+1)
    break
col_start = 0
row_start = 0
col_end = 3 
row_end = 3
test_sect = False

for line in range(0, 9):
  sect_check = []
  sect_total = 0
  if line == 1:
    col_start = 3
    col_end = 6
  elif line == 2:
    col_start = 6
    col_end = 9
  elif line == 3:
    row_start = 3
    row_end = 6
    col_start =0
    col_end = 3
  elif line ==4:
    col_start =3
    col_end = 6
  elif line == 5:
    col_start = 6
    col_end=9
  elif line == 6:
    row_start = 6
    row_end = 9
    col_start =0
    col_end = 3
  elif line ==7:
    col_start =3
    col_end = 6
  elif line == 8:
    col_start = 6
    col_end=9
  for col in range(col_start, col_end):
    for row in range(row_start, row_end):
      sect_check.append(board[row][col])
  print("==="*5)
  print(sect_check)
  for elements in sect_check:
    sect_total += int(elements)
  print(sect_total)
  if sect_total == 45:
    test_sect = True
    continue
  else:
    test_sect=False
    print("No")
    print("Error in section ", line+1)
    break


if test_col and test_row and test_sect:
  print("Yes")


#invalid soduku
"""
195743862
432865917
876192543
387459216
612387495
549216738
763524189
928671354
254938671
"""

#Valid soduku
"""
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""
