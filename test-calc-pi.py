# Leibniz formula for π
# Initialize variables

pi = 0
number_of_iterations = 100000  # The more iterations, the more accurate the value of pi.

# Calculate pi using the Leibniz formula
for i in range(number_of_iterations):
    pi += ((-1) ** i) / (2 * i + 1)

pi *= 4  # Multiply by 4 to get the final value

# Print the calculated value of pi
print(f"The calculated value of pi after {number_of_iterations} iterations is: {pi}")

# Chudnovsky algorithm for π
from decimal import Decimal, getcontext

# Set the precision to 102 places; extra precision is needed for intermediate steps
getcontext().prec = 1002

def compute_pi(n_terms):
    # Constants used in the Chudnovsky algorithm
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, n_terms):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        K += 12
        S += Decimal(M * L) / X

    pi = C / S
    return pi

# Number of terms - this might need adjustment to get exactly 100 digits
n_terms = 20
pi = compute_pi(n_terms)

# Print pi to 100 decimal places
print(f"Pi to 100 decimal places: {str(pi)[:1001]}")
