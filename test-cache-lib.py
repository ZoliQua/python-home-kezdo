# Based on Medium article
# URL: https://towardsdatascience.com/functools-an-underrated-python-package-405bbef2dd46

from functools import lru_cache
import timeit

def factorial(n):
    return n * factorial(n-1) if n else 1

@lru_cache
def factorial_cached(n):
    return n * factorial(n-1) if n else 1

# Console write:
# >>> %timeit factorial(10)
# 989 ns ± 16.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# >>> %timeit factorial(15)
# 1.49 µs ± 12.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# >>> %timeit factorial_cached(10)
# 57.7 ns ± 0.417 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
# >>> %timeit factorial_cached(10)
# 57.6 ns ± 1.08 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

