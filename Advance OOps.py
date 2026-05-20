class Myclass(object):
    def __init__(self):
        pass
    def display(self):
        print('I am Method')

x=Myclass()
x.display()

class Mobile:
    def __init__(self):
        self.model='RealmeX'
    def display(self):
        print("model:",self.model)
x=Mobile()
x.display()
x.model='OnePlus11R'
print(x.model)
x.display()

class Mobile:
    def __init__(self):
        self.model="RealmeX"
    def display(self):
        self.price=10000
        print("Model:",self.model,'And Price:',self.price)
x=Mobile()
x.display()

class Mobile:
    def __init__(self,m):
        self.model = m

    def display(self,n):
        self.price = n
        print("Model:", self.model, "And Price:", self.price)
x = Mobile("One Plus11R")
x.display(20000)


class Mobile:
    def __init__(self, m):
        self.model = m

    def display(self, n):
        self.price = n
        print("Model:", self.model, "And Price:", self.price)


x = Mobile("One Plus11R")
x.display(20000)

class Mobile:
    def __init__(self, m):
        self.model = m

    def display(self, n):
        self.price = n
        print("Model:", self.model, "And Price:", self.price)


x = Mobile("One Plus11R")
x.display(20000)
print(id(x))
y=Mobile("RealmeX")
y.display(15000)
print(id(y))

z=Mobile("Vivo")
z.display(13000)
print(id(z))
