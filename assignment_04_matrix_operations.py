# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
=============================================================================
def read_matrix(rows, cols):
	matrix = []
	for r in range(1, rows + 1):
		while True:
			try:
				row = input(f"Enter row {r}: ").strip().split()
				if len(row) != cols:
					print(f"Please enter exactly {cols} values.")
					continue
				matrix.append([float(x) if ('.' in x or 'e' in x.lower()) else int(x) for x in row])
				break
			except ValueError:
				print("Invalid number. Try again.")
	return matrix


def display_matrix(mat):
	if not mat:
		print("[]")
		return
	# determine column widths
	cols = len(mat[0])
	widths = [0] * cols
	for r in mat:
		for j, val in enumerate(r):
			widths[j] = max(widths[j], len(str(val)))
	for r in mat:
		line = " ".join(str(val).rjust(widths[j]) for j, val in enumerate(r))
		print(line)


def transpose_matrix(mat):
	if not mat:
		return []
	rows = len(mat)
	cols = len(mat[0])
	trans = [[None for _ in range(rows)] for _ in range(cols)]
	for i in range(rows):
		for j in range(cols):
			trans[j][i] = mat[i][j]
	return trans


def add_matrices(a, b):
	rows = len(a)
	cols = len(a[0])
	res = [[0 for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			res[i][j] = a[i][j] + b[i][j]
	return res


def multiply_matrices(a, b):
	m = len(a)
	n = len(a[0])  # also rows of b
	p = len(b[0])
	res = [[0 for _ in range(p)] for _ in range(m)]
	for i in range(m):
		for j in range(p):
			s = 0
			for k in range(n):
				s += a[i][k] * b[k][j]
			res[i][j] = s
	return res


def read_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter an integer.")


def part_a():
	print("PART A — Transpose a Matrix")
	r = read_int("Enter number of rows: ")
	c = read_int("Enter number of columns: ")
	a = read_matrix(r, c)
	print("Original Matrix:")
	display_matrix(a)
	t = transpose_matrix(a)
	print("Transposed Matrix:")
	display_matrix(t)


def part_b():
	print("PART B — Add Two Matrices")
	r = read_int("Enter number of rows: ")
	c = read_int("Enter number of columns: ")
	print("First matrix:")
	a = read_matrix(r, c)
	print("Second matrix:")
	b = read_matrix(r, c)
	print("Sum of matrices:")
	display_matrix(add_matrices(a, b))


def part_c():
	print("PART C — Multiply Two Matrices")
	m = read_int("Enter number of rows for matrix A: ")
	n = read_int("Enter number of columns for matrix A (and rows for B): ")
	p = read_int("Enter number of columns for matrix B: ")
	print("Matrix A:")
	a = read_matrix(m, n)
	print("Matrix B:")
	b = read_matrix(n, p)
	print("Product matrix A x B:")
	display_matrix(multiply_matrices(a, b))


def main():
	part_a()
	print()
	part_b()
	print()
	part_c()


if __name__ == "__main__":
	main()

