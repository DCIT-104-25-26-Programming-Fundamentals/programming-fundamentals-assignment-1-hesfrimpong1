# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
=============================================================================
def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	if b == 0:
		raise ZeroDivisionError
	return round(a / b, 2)


def modulus(a, b):
	if b == 0:
		raise ZeroDivisionError
	return a % b


def exponent(a, b):
	return a ** b


def print_menu():
	print("=============================")
	print("     SIMPLE CALCULATOR")
	print("=============================")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Modulus")
	print("6. Exponentiation")
	print("7. Quit")


def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Invalid number. Try again.")


def main():
	while True:
		print_menu()
		choice = input("Select an operation (1-7): ").strip()

		if choice == '7':
			print("Goodbye!")
			break

		if choice not in {'1','2','3','4','5','6'}:
			print("Invalid choice. Please select a number between 1 and 7.")
			continue

		a = get_number("Enter first number : ")
		b = get_number("Enter second number: ")

		try:
			if choice == '1':
				result = add(a, b)
				op = '+'
			elif choice == '2':
				result = subtract(a, b)
				op = '-'
			elif choice == '3':
				result = multiply(a, b)
				op = '*'
			elif choice == '4':
				result = divide(a, b)
				op = '/'
			elif choice == '5':
				result = modulus(a, b)
				op = '%'
			elif choice == '6':
				result = exponent(a, b)
				op = '**'

			# Format division to two decimals; others show as-is (but remove .0 when integer)
			if choice == '4':
				print(f"Result: {a} {op} {b} = {result:.2f}")
			else:
				# display integer-like numbers without .0
				def fmt(x):
					if isinstance(x, float) and x.is_integer():
						return str(int(x))
					return str(x)

				print(f"Result: {fmt(a)} {op} {fmt(b)} = {fmt(result)}")

		except ZeroDivisionError:
			print("Error: Cannot divide by zero.")


if __name__ == '__main__':
	main()


