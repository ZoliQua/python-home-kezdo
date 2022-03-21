
# LIST Basics

tomb = ['V', "C", "Ő", "O", "A", "K", "H"]
tomb.sort()
print(tomb)
print(tomb[2:2])

# Creating a new, one element list
tomb2 = ['nem']

# last element of a list
print(tomb[-1])

# Slicing (minus the first element)
print(tomb[1:])

# Multi dimension list
tartomany = range(100)
print(list(tartomany))

for i in range(10):
    print("Szevasz", i)

# Creating fibonacci series
fibo = [0, 1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(50)]

