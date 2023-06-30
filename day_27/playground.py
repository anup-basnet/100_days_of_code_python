# *args and **kwargs

# CHALLENGE: Modify the add function to take an unlimite number of arguments . Use a loop to sum all the arguments inside the function. Test it out by calling add() to calculate sum of some arguments.


def add(*args):
    sum = 0
    for num in args:
        sum += num
    print(sum)


add(2, 3, 5)


## **kwargs
def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.seats = kw["seats"]


my_car = Car(make="Nissan", seats=4)
print(my_car.model)
