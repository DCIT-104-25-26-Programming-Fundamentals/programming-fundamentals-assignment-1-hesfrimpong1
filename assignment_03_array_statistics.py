# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
=============================================================================
def calc_sum(numbers):
	total = 0
	for n in numbers:
		total += n
	return total


def calc_average(numbers):
	if len(numbers) == 0:
		return 0
	return calc_sum(numbers) / len(numbers)


def calc_max(numbers):
	if len(numbers) == 0:
		return None
	current_max = numbers[0]
	for n in numbers[1:]:
		if n > current_max:
			current_max = n
	return current_max


def calc_min(numbers):
	if len(numbers) == 0:
		return None
	current_min = numbers[0]
	for n in numbers[1:]:
		if n < current_min:
			current_min = n
	return current_min


def format_number(n):
	# Print as int if whole number, else as float
	if isinstance(n, float) and n.is_integer():
		return str(int(n))
	return str(n)


def main():
	try:
		count = int(input("How many numbers? "))
	except ValueError:
		print("Invalid input. Expected an integer.")
		return

	if count <= 0:
		print("Error: N must be a positive integer.")
		return

	numbers = []
	for i in range(1, count + 1):
		while True:
			try:
				val = float(input(f"Enter number {i}: "))
				numbers.append(val)
				break
			except ValueError:
				print("Invalid number. Please enter a numeric value.")

	total = calc_sum(numbers)
	avg = calc_average(numbers)
	maximum = calc_max(numbers)
	minimum = calc_min(numbers)

	print("\nResults:")
	print("Sum:     ", format_number(total))
	print("Average: ", format_number(avg))
	print("Maximum: ", format_number(maximum))
	print("Minimum: ", format_number(minimum))


if __name__ == "__main__":
	main()


