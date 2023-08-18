def print_matrix_indices(matrix, row_pointer, col_pointer, n, m, direction):
  if row_pointer == n or col_pointer == m:
    return
  print(f'[{row_pointer}, {col_pointer}]', end=' ')
  if direction == 'right':
    if col_pointer + 1 < m:
      print_matrix_indices(matrix,row_pointer, col_pointer + 1, n, m, "right")
    else:
      print_matrix_indices(matrix, row_pointer + 1, col_pointer, n, m, 'left')

  elif direction == "left":
    if col_pointer - 1 >= 0:
      print_matrix_indices(matrix, row_pointer, col_pointer - 1, n, m, "left")
    else:
      print_matrix_indices(matrix, row_pointer + 1, col_pointer, n, m, 'right')

def show_matrix_indices(matrix):
  n = len(matrix)
  m = len(matrix[0])
  print_matrix_indices(matrix, 0, 0, n, m, 'right')

matrix = [[1, 2, 3, 0],
          [4, 5, 6, 0],
          [7, 8, 9, 0]]

show_matrix_indices(matrix)
