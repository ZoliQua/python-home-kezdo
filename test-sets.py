#
# This file is test is for set type
#


# See the intersection of set A0 and set B0
A0 = {1, 2, 3}
B0 = {3, 4, 5}
print("SetA0 is", A0)
print("SetB0 is", B0)
result = A0.intersection(B0)
print(f"Intersection of setA0 and setB0 is: {result}.")
print("")

# See the intersection of set A, set B and set C
A = {1, 2, 3, 4, 5}
B = {2, 3, 4, 10, 11}
C = {100, 3, 8, 2, 1, 4}
D = {1, 2, 3}
print("SetA type is", type(A), ", contains:", A)
print("SetB is", type(B), ", contains:", B)
print("SetC is", type(C), ", contains:", C)
print("SetD is", type(D), ", contains:", D)

result2a = A.intersection(B, C)
print(f"Intersection of setA, setB and setC are: {result2a}.")
result2b = A.intersection(B, C, D)
print(f"Intersection of setA, setB, setC and setD are: {result2b}.")

# See the union of set A and set B
result3 = A.union(B)
print(f"Union of setA and setB: {result3}.")

# See the union of set A, set B and set C
result4 = A.union(B, C)
print(f"Union of setA, setB and setC: {result4}.")

# See the difference of set A and set B
result5 = A.difference(B)

# See the symmetric difference of set A and set B
result6 = A.symmetric_difference(B)
print(f"Symmetric difference of setA and setB: {result6}.")

# See if set D is a subset of set A
result7 = D.issubset(A)
print(f"Is setD a subset of setA?: {result7}.")

# See if set B is a subset of set A
result8 = B.issubset(A)
print(f"Is setB a subset of setA?: {result8}.")
