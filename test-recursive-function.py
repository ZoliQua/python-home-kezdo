
# Base example - factorial

def factorial(n):

	if n == 0 or n == 1:
		return 1

	return n * factorial(n - 1)


# Iterate a list without loops


def iterateLista(array):

	if len(array) == 0:
		return True

	print(f"Element\t{array.pop()}")

	return iterateLista(array)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterateLista(lista)

# Decide if the string is a palindrome with recursive function


def PalindromeDecider(sample):

	if not isinstance(sample, str):
		return False

	length = len(sample)

	if length < 1:
		return False
	elif length == 1:
		return True
	else:
		if sample[0] == sample[-1]:
			if length < 3:
				return True
			else:
				return PalindromeDecider(sample[1:-1])
		else:
			return False

test_list = ["okos_vagyok", "adnabelefelebanda", "hamis_simah", "moww", "my_ aa _ym"]

for element in test_list:
	print("Test: OK", element) if PalindromeDecider(element) else print("Test: FAILED", element)





