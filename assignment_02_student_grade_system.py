# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter student score (0-100): 85
#   Grade: A
#
#   Enter student score (0-100): 73
#   Grade: B
#
#   Enter student score (0-100): 45
#   Grade: F
#
#   Enter student score (0-100): 110
#   Error: Score must be between 0 and 100.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST use functions (see scaffold below).
# - Validate that the score is within the range 0–100 inside get_grade().
#   If it is not, return None and let main() print the error message.
# - Use if / elif / else to determine the grade.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
=============================================================================
def get_grade(score):
	"""Return letter grade for score (0-100). Return None if score out of range."""
	try:
		# Ensure score is an integer (or can be compared as number)
		s = int(score)
	except Exception:
		return None

	if s < 0 or s > 100:
		return None

	if 80 <= s <= 100:
		return 'A'
	elif 70 <= s <= 79:
		return 'B'
	elif 60 <= s <= 69:
		return 'C'
	elif 50 <= s <= 59:
		return 'D'
	else:
		return 'F'


def main():
	user = input('Enter student score (0-100): ')
	grade = get_grade(user)
	if grade is None:
		print('Error: Score must be between 0 and 100.')
	else:
		print(f'Grade: {grade}')


if __name__ == '__main__':
	main()


