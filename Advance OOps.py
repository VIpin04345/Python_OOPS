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


# 🔹 Level 1 (Basic Understanding)

# Q1.
# Ek Student class banao jisme:

# attributes: name, marks
# method: display() jo details print kare


class Student(object):
    def __init__(self):
        self.name = "Shubham Yadav"
        self.marks = 95

    def display(self):
        print("Name:", self.name, "And Marks:", self.marks)


obj = Student()
obj.display()


class Car(object):
    def __init__(self):
        self.brand='Supra'
        self.speed=250

    def accelerate(self):
        s=self.speed+10
        print('speed after accelerate:',s)
    def brake(self):
        b=self.speed-5
        print('speed after brake:',b)

obj=Car()
obj.accelerate()
obj.brake()


class Ractangle(object):
    def __init__(self):
        self.length = 10
        self.breath = 5

    def area(self):
        print("Area:", self.length * self.breath)

    def perimeter(self):
        result = 2 * (self.length + self.breath)
        print("Perimeter:", result)


obj = Ractangle()
obj.area()
obj.perimeter()



class BankAccount(object):
    def __init__(self):
        self.balance = 1000

    def deposit(self, ammount):
        print("Your actual balance is", self.balance)
        self.balance += ammount
        print("Your balance after deposit:", self.balance)

    def withdraw(self, ammount):
        if self.balance >= 1000:
            self.balance -= ammount
        print("your balance after withdraw:", self.balance)


BankAccount()
obj.deposit(500)
obj.withdraw(100)


class Employee(object):
    def __init__(self):
        self.salary = 1000

    def inc_sal(self):
        print("salary before increment:", self.salary)
        self.salary += 500
        print("salary after increment:", self.salary)


obj = Employee()
obj.inc_sal()
