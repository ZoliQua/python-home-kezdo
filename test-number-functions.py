#
# Testing the basic number functions of python
#

# My first python file

szam1 = 14
szam2 = 12

# addition - összeadás
print(szam1+szam2)
# subtraction - kivonás
print(szam1-szam2)
# multiplication - szorzás
print(szam1*szam2)
# division - osztás
print(szam1/szam2)
# division to whole number - egészre osztás
print(szam1//szam2)
# exponentiation - hatványozás
print(szam1**szam2)
# modulation
print(szam1%szam2)

"""
OPERATORS
<
>
<=
>=
!=
==
"""

"""
TEST FOR A CYCLE
a = 0
while a <= 10:
    a = a + 1
    print(a)
"""


def check(numbers):
    for i in numbers:
        if i == 0:
            print("0 is present")
    else:
        print("0 is not present")


check([1, 2, 3, 4])  ### 0 not present
check([0, 1, 2])  ## 0 present
