class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on it, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        # if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                # raise AttributeError("Testing exception handler in migrate")
            except AttributeError as e:
                print("One duck down")
                problem = e
        if problem:
            raise problem


flock = Flock()
donald = Duck()
daisy = Duck()
duck3 = Duck()
duck4 = Duck()
duck5 = Duck()
duck6 = Duck()
duck7 = Duck()
percy = Penguin()
mallard = Mallard()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)
flock.add_duck(percy)  # no fly method
flock.add_duck(mallard)

flock.migrate()
