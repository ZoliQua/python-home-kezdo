# SOURCE: https://python.plainenglish.io/how-i-calculated-the-1-000-000th-fibonacci-number-with-python-e921d3642dbf

from functools import lru_cache
import sys
import decimal

sys.setrecursionlimit(10000)


@lru_cache()
def recursiveFibCached(n):
    if n == 1 or n == 2:
        return 1

    return recursiveFibCached(n - 1) + recursiveFibCached (n - 2)


print(recursiveFibCached(6))


def iterativeFib(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a

print(iterativeFib(6))



def formulaFibWithDecimal(n):
    decimal.getcontext().prec = 100000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)

print(formulaFibWithDecimal(89200))