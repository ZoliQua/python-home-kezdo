# Python Test Project File
# Written by Zoltan Dul (2021)
#
# Python program to demonstrate
# defaultdict funcion from collections

# Import
from collections import defaultdict


# Function to return a default
# values for keys that is not
# present

def def_value():
	return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
print(d["d"])
