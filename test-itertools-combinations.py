
from itertools import combinations, permutations
from collections import Counter
import string
import numpy as np

# Functions
# Print item by line


def PrintR(a_list_to_print, inString=False):
	counter = 0
	for element in a_list_to_print:
		counter += 1
		if inString is False:
			print(f"\t\t{counter}\t{element}")
		else:
			print(f"\t\t{counter}\t{''.join(element)}")
	return True


# Simple combinations of five numbers

list_of_numbers = [1, 2, 3, 4, 5]
print("Length 2: ", list(combinations(list_of_numbers, 2)))
print("Length 3: ", list(combinations(list_of_numbers, 3)))

# Simple permutation of three numbers

perm = list(permutations([1, 2, 3]))
print(perm)

####################################################################
# Permutation of a given number of characters from ascii_uppercase #
####################################################################

# Set number of characters
char_num = 6
# Create a list of characters based on char_num
chars = list(string.ascii_uppercase)[0:char_num]

for i in range(1, len(chars)):
	num = i + 1
	this_chars_len = 0
	print(f"Combination of {num} characters")
	print("="*30)
	for j in range(1, num+1):
		this_combination = list(combinations(chars[:num], j))
		this_combination_len = len(this_combination)
		this_chars_len += this_combination_len
		print(f"{num} chars in {j} combination ({this_combination_len} element(s)):")
		PrintR(this_combination, True)

	print("\t"*10)
	print(f"There were {this_chars_len} combinations for {num} chars.")
	print("\t"*10)

	# print(f"Char {num} permutation: {list(permutations(chars[:num]))}")



random_elements = np.random.randint(0, 10, 100)
dict_freq = Counter(random_elements)
print(dict_freq)
