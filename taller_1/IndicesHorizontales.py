def print_matrix_indices(matrix, row, col, n, m, direction):
  if row >= n or col >= m:
    return
  print(f'[{row}, {col}]', end=' ')
  if direction == 'right':
    if col + 1 < m:
      print_matrix_indices(matrix, row, col + 1, n, m, direction)
    else:
      print_matrix_indices(matrix, row + 1, col, n, m, 'left')
  else:
    if col - 1 >= 0:
      print_matrix_indices(matrix, row, col - 1, n, m, direction)
    else:
      print_matrix_indices(matrix, row + 1, col, n, m, 'right')

def show_matrix_indices(matrix):
  n = len(matrix)
  m = len(matrix[0])
  print_matrix_indices(matrix, 0, 0, n, m, 'right')

matrix = [[1, 2, 3, 0],
          [4, 5, 6, 0],
          [7, 8, 9, 0]]

show_matrix_indices(matrix)
