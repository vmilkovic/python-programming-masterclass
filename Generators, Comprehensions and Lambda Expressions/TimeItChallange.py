# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit
from statistics import stdev, mean


fact_test = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

x = fact(130)
"""

factorial_test = """\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
        
y = factorial(130)
"""

print(timeit.timeit(fact_test, number=10000))
print(timeit.timeit(factorial_test, number=10000))


# or we can import as a module
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":

    print()

    print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=1000))
    print(timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=1000, repeat=6))

    list_1 = timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=1000, repeat=6)
    print(mean(list_1), stdev(list_1))

    print()

    print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number=1000))
    print(timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=1000, repeat=6))

    list_2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=1000, repeat=6)
    print(mean(list_2), stdev(list_2))
