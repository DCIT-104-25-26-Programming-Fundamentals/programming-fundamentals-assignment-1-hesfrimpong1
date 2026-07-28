# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
=============================================================================
def multiplication_table(n: int) -> None:
	"""Print multiplication table for n from 1 to 12."""
	print(f"Multiplication Table for {n}:")
	for i in range(1, 13):
		print(f"{n}  x  {i}  =  {n * i}")


def part_a() -> None:
	"""Part A — Single Table: ask user for a number and print its table."""
	try:
		value = int(input("Enter a number for a single multiplication table: ").strip())
	except ValueError:
		print("Error: please enter a valid integer.")
		return
	multiplication_table(value)


def part_b() -> None:
	"""Part B — Tables from 1 to N: ask user for N and print tables 1..N."""
	try:
		n = int(input("Enter a positive integer N to print tables from 1 to N: ").strip())
	except ValueError:
		print("Error: please enter a valid integer.")
		return
	if n <= 0:
		print("Error: N must be a positive integer.")
		return
	for num in range(1, n + 1):
		multiplication_table(num)
		if num != n:
			print("---------------------------")


if __name__ == "__main__":
	part_a()
	print()
	part_b()





