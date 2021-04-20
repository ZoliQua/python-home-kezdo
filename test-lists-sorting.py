#
# Test to sort different lists in Python
# Written by Zoltan Dul, DMD, Phd
# 2021
#


#
# Testing the sorting of lists
#

lst = [9, 2, 1, 6, 4, 5, 7, 8, 3]
lst2 = [9, 2, 1, 6, 4, 5, 7, 8, 3]

lst.sort()
print(lst)

#
# Sorting in normal order
#

sorted_lst = sorted(lst2)

print(f'Sorted list: {sorted_lst}')
print(f'Original list: {lst2}')

#
# Sorting in reverse order
#

sorted_lst_reverse = sorted(lst, reverse=True)
print(f'Sorted list (reverse): {sorted_lst_reverse}')

#
# Sorting dictionaries
#

dct = {
    'Tom': 33,
    'Harry': 23,
    'Ron': 87,
    'John': 13
}

sorted_dct = sorted(dct)
sorted_dct_items = sorted(dct.items())
sorted_dct_reverse = sorted(dct.items(), key=lambda x: x[1])

print(f'Sorted dictionary (by dict): {sorted_dct}')
print(f'Sorted dictionary (by items): {sorted_dct_items}')
print(f'Sorted dictionary (by values): {sorted_dct_reverse}')
print(dct)
print(dct.items())
print(dct.keys())
print(dct.values())

#
# Test for getting index of a list
#

rnd_list = [1, 2, 3, 1, 1]
testrr = [index for index, value in enumerate(rnd_list) if value == 1]
print(testrr)

#
# Extract  a list in one line into three different variables
#
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print("Value a:", a)
print("Value b:", b)
print("Value c:", c)

#
# Merge two different lists into one
#

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print("Merged List:", my_merged_list)

#
# String to a List
#

a_list = [*"RealPython"]
print("A list from string:", a_list)
