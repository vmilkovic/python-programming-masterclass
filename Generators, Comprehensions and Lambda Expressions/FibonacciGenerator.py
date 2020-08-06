
def fibonacci():
    current, previous = 0, 1
    while True:
        current, previous = current + previous, current
        yield current


fib = fibonacci()

for i in range(20):
    print(next(fib))
