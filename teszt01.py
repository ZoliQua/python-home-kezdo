szam1 = 14
szam2 = 12

# összeadás
print(szam1+szam2)
# kivonás
print(szam1-szam2)
# szorzás
print(szam1*szam2)
# osztás
print(szam1/szam2)
# egészre osztás
print(szam1//szam2)
# hatványozásR
print(szam1**szam2)
# modulo
print(szam1%szam2)

"""
OPERATOROK
<
>
<=
>=
!=
==
"""

"""
CIKLUS TESZT
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
