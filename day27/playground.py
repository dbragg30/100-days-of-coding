def add(*args):
    sum = 0
    for n in args:
        sum += n / 1.5
    return sum


#print(add(1, 2, 3, 4, 200, 2, 1000))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline",color="blue")
print(my_car.model, my_car.color)



