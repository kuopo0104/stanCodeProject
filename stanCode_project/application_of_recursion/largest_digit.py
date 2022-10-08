"""
File: largest_digit.py
Name:Neil
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))  	  # 9


def find_largest_digit(n):
	return find_largest_digit_helper(abs(n), get_the_num(n))


def find_largest_digit_helper(n: int, maximum: int) -> int:
	candidate = get_the_num(n)
	if candidate > maximum:
		maximum = candidate

		# Recursion
	if go_to_next_num(n) == 1:	 # Check all the number in the digit(int have no index)
		return maximum
	else:
		next = go_to_next_num(n)
		return find_largest_digit_helper(next, maximum)


def get_the_num(number):
	n = 0
	i = 0
	while True:
		if number < 10:
			break
		if 10 ** n >= number:
			while (10 ** (n - 1)) * i < number:
				i += 1
			return i-1
		else:
			n += 1
	return number


def go_to_next_num(number):
	n = 0
	i = 0
	while True:
		if 10 ** n >= number:
			while (10 ** (n - 1)) * i < number:
				i += 1
			break
		else:
			n += 1
	new_number = number - 10 ** (n-1) * (i-1)
	return new_number


if __name__ == '__main__':
	main()
