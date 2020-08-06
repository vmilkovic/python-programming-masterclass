def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()
for x in range(10000000):
    print(next(approx_pi))

