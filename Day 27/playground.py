def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5,3,4,5,7,1))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


calculate(2, add = 3, multiply = 5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"] # if not typed, there will be an error
        self.model = kw.get("model") # difference between .get() and [] is that
        # if there's no such argument in function() while coding, then it returns None

my_car = Car(make = "Nissan", model = "GTR")
print(my_car.model)

def test(*args):
    print(args)


test(1, 2, 3, 5) # tuple data type.
# Tuples are immutable and efficient for storing a fixed sequence of values.
