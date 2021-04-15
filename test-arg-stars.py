
def f(a, b):
	print(a, b)

args = { "a": 1, "b": 2 }

# Passing arguments with two stars (**)
f(**args)

args_list =  [1, 2]

# Passing arguments with one star (**)
f(*args_list)