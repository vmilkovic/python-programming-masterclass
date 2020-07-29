# Recursion exception
def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculate n! recursively """
    if n <= 1:
        return 1
    else:
        print(n/0)
        return n * factorial(n - 1)


try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError, OverflowError):
    print("This program can't calculate factorial that large!!")
except ZeroDivisionError:
    print("What are you doing dividing by zero????")

print("Program terminating")
