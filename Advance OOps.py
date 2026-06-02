class Myclass(object):
    def __init__(self):
        pass
    def display(self):
        print('I am Method')

x=Myclass()
x.display()

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






class Mobile():
    def __init__(self):
        print("this is constructor class:")
obj=Mobile()

class Mobile():
    def __init__(self):
        print("this is constructor class:")
obj=Mobile()

class Mobile:
    def __init__(self,m,v=80):
        self.mobile=m
        self.speed=v

    def show(self,p):
        self.price=p
        print('model:',self.mobile,'price:',self.price)
        print("volume:",self.speed)

obj=Mobile("realmeX")
obj.show(1000)
print(id(obj))

class Mobile:
    def __init__(self,m,v=80):
        self.mobile=m
        self.speed=v

    def show(self,p):
        self.price=p
        print('model:',self.mobile,'price:',self.price)
        print("volume:",self.speed)

obj=Mobile("realmeX")
obj.show(1000)
print(id(obj))


obj1=Mobile("Oneplus",100)
obj1.show(2000)
print(id(obj1))



class Mobile:
    fp = "Yes"

    def __init__(self):
        self.model = "RealmeX"

    def show(self):
        print("Model:", self.model)

    @classmethod
    def is_fp(cls):
        print("finger print", cls.fp)

realme = Mobile()
redmi=Mobile()
geek=Mobile()
print()
Mobile.is_fp ='No'


print(Mobile.fp)
print(Mobile.fp)
print(Mobile.fp)

class Mobile(object):
    fp = "YES"

    def __init__(self):
        self.model = "RealmeX"

    def show(self):
        print("Model:", self.model)

realme = Mobile()
redmi = Mobile()
oneplus = Mobile()

print("Class FP:", Mobile.fp)
print("realme FP:", realme.fp)
print("redmi FP:", redmi.fp)
print("oneplus FP:", oneplus.fp)
print()
Mobile.fp='NO'
print("Class FP:", Mobile.fp)
print("realme FP:", realme.fp)
print("redmi FP:", redmi.fp)
print("oneplus FP:", oneplus.fp)
print()
realme.fp='Not Working'
oneplus.fp='hex dynamic'
print("Class FP:", Mobile.fp)
print("realme FP:", realme.fp)
print("redmi FP:", redmi.fp)


class Mobile:
    def show(self):
        print("RealmeX")
realme=Mobile()
realme.show()

class Mobile:
    def __init__(self,m):
        self.moodel=m
    def show(self,p):
        self.price=p
        print("Model:",self.moodel,'And Price:',self.price)
realme=Mobile('RealmeX')
realme.show(1000)



class Mobile:
    def __init__(self):
        self.model = "RealmeX"

    def get_model(self):
        return self.model


realme = Mobile()
m = realme.get_model()
print(m)

class Mobile:
    def __init__(self):
        self.model = "RealmeX"

    def get_model(self):
        return self.model


realme = Mobile()
m = realme.get_model()
print(m)




class Mobile:
    def __init__(self):
        self.model = "RealmeX"

    def set_model(self):
        self.model = "Realme 2"


realme = Mobile()
# realme.model
realme.set_model()
print(realme.model)




class Mobile:
    fp='Yes'
    def __init__(self):
        self.moodel="RelmeX"
    @classmethod
    def show_model(cls):
        print(cls.fp)
realme=Mobile()
Mobile.show_model()
print(Mobile.fp)


class Mobile:
    fp = "Yes"

    def __init__(self):
        self.moodel = "RelmeX"

    @classmethod
    def show_model(cls, r):
        cls.ram = r
        print("fingerprint:",cls.fp)
        print('RAM:',cls.ram)
realme = Mobile()
Mobile.show_model("4GB")
print(Mobile.fp)



class Student:
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    def disp(self):
        print("name:", self.name)
        print("roll:", self.roll)


class User:
    @staticmethod
    def show(s):
        print("user name", s.name)
        print("user roll:", s.roll)
        s.disp()


stu = Student("Akash", 101)
User.show(stu)


class Army:
    def __init__(self):
        self.name='rahul'
        self.gn=self.Gun()
    def show(self):
        print("name:",self.name)

    class Gun:
        def __init__(self):
            self.name="AK47"
            self.capacity='75 rounds'
            self.length='34.3 In'
        def disp(self):
            print('gun name:',self.name)
            print('capacity:',self.capacity)
            print('length:',self.length)

a=Army()
print(a.name)
a.show()

print(a.gn.name)
a.gn.disp()

g=a.gn
print(g.name)
g.disp()





class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            print("name:", self.name, "Grade:", "A")
        elif self.marks >= 75:
            print("name:", self.name, "grade:", "B")
        else:
            print("grade:", "C")


obj = Student("Rohit", 78)
obj.grade()



class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, discount):
        discount_price = (self.price * discount) / 100
        final_price = self.price - discount_price
        print("Model:", self.brand, "final price:", final_price)


obj = Mobile("RealmeX", 20000)
obj.discount(50)




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        if self.age >= 18:
            print("True")
        else:
            print("False")


obj = Person("raghav", 122)
obj.is_adult()




class Car:
    def __init__(self,brand):
        self.brand=brand
    def show(self,s):
        self.s=s
        print("brand Name:",self.brand,'Speed:',self.s)


obj=Car('Supra')
obj.show(260)
obj1=Car('Lambo')
obj1.show()


class Car:
    def __init__(self,speed,name):
        self.speed=speed
        self.name=name
    def show(self):
        print('Car name is:',self.name,'Speed is:',self.speed)


obj1=Car(name='Supra',speed=98)
obj1.show()
obj2=Car('Lambo','100')
obj2.show()


class Laptop:
    def __init__(self,name , ram , price):
        self.name=name
        self.ram=ram
        self.price=price
    def show(self):
        print('Name:',self.name,'\nRam:',self.ram,'\nprice:',self.price)

obj1=Laptop('Lenovo','12GB',50000)
obj1.show()
obj2=Laptop("Dell",'8GB',40000)
obj2.show()



class BankAccount:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def deposit(self, ammount):
        self.ammount = ammount
        print("Name:", self.username)
        print("Your currunt balance is:", self.balance)
        deposit = self.balance + self.ammount
        print("Your balance after deposit:", deposit)

    def withdraw(self):
        if self.balance > self.ammount:
            withdraw = self.balance - self.ammount
            print("Your balance after withdraw:", withdraw)

obj1 = BankAccount("Shubh", 1000)
obj1.deposit(500)
obj1.withdraw()


obj2 = BankAccount("Vip", 100000)
obj2.deposit(5000)
obj2.withdraw()


class Student:
    school_name = "XYZ International School"

    def __init__(self, name):
        self.name = name

    def show(self, classes, mobile, age):
        self.classes = classes
        self.mobile = mobile
        self.age = age
        print(
            "School name:",
            Student.school_name,
            "Name Of Student:",
            self.name,
            "\n Class Name:",
            self.classes,
            "\n Mobile no:",
            self.mobile,
            "\n And age:",
            self.age,
        )

obj1 = Student("Akash")
obj1.show(8, 9687959685, 12)
obj2 = Student("Vimal")
obj2.show(10, 9867890976, 16)


class Employee:
    company_name = "XYZ Tech PVT LTD"

    def __init__(self, emp_name):
        self.name = emp_name

    def show(self):
        print("Company:", Employee.company_name, "Employee Name:", self.name)

         @classmethod
    def change_classname(cls, new_name):
        cls.company_name = new_name


obj = Employee("Vipin Yadav")
obj1 = Employee("Shubham Yadav")
obj.show()
obj1.change_classname("TCS")
obj1.show()


class Car:
    wheels = 4

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name, "Wheels:", self.wheels)

obj1 = Car("Supra")
obj2 = Car("Mustang")

obj2.wheels = 6  # override for this object only

obj1.show()
obj2.show()
print("Class wheels:", Car.wheels)


class Car:
    wheels = 4

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name, "Wheels:", self.wheels)

obj1 = Car("Supra")
obj2 = Car("Mustang")

obj2.wheels = 6  # override
obj1.show()  # 4
obj2.show()  # 6

class Game:
    max_player=4
    def __init__(self,name):
        self.name=name
    def show(self):
        print("name:",self.name,'Players:',self.max_player)
obj1=Game("Ludo")
obj2=Game("carrom")
obj3=Game("cricket")
obj3.max_player=11
obj1.show()
obj2.show()
obj3.show()


class Bank:
    interest_rate = 7.5  # class variable (sabke liye same)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show(self):
        print("Name:", self.name)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)

obj1 = Bank("Shubham", 1000)
obj2 = Bank("Vipin", 5000)

obj1.show()
obj2.show()


class Collage:
    clg_name = "XYZ Group Of Institutions"

    def __init__(self, name):
        self.name = name

    def show(self):
        print("collage name:", Collage.clg_name, "Name:", self.name)


obj1 = Collage("Shubham Yadav")
obj2 = Collage("Vipin Yadav")

obj1.show()
obj2.show()ndsjndijdfij



class Student:
    def __init__(self, __marks):
        self.__marks = __marks

    def get_marks(self):
        return self.__marks

obj = Student(200)
m = obj.get_marks()
print(m)



class Person:
    def __init__(self,age):
        self.__age=age
    def get_age(self):
        if self.__age<0:
            return "Invalid Age"
        else:
            return self.__age

obj=Person(18)

print(obj.get_age())
