class hello:
    def ram(self):
        a=12
        b=13
        c=a+b
        print(c)

s=hello()
s.ram()





class Some():
    def loop(self):
        i=1
        while(i<=10):
            print(i)
            i+=1
    
s=Some()
s.loop()



class Ram():
    def sum(self):
        n=int(input('enter a number:-'))
        n1=int(input('enter secont number:-'))
        sum=n+n1
        print(sum)
a=Ram()
a.sum()




class Father:
    def f1(self):
        print('father class')
class Child(Father):
    def c1(self):
        print('child class')
        
s=Child()
s.f1()
s.c1()

class Student:
    name='karan'
    def __init__(self,name):
        self.name=name
        print('adding new student')
obj=Student('karan')
print(obj.name)





class Car:
    def __init__(self,carname,brand):
        self.carname=carname
        self.brand=brand
obj=Car('thar','toyota')
print(obj.carname)
print(obj.brand)




class Student:
    @staticmethod
    def hello():
        print('hello worls')
obj=Student()
obj.hello()



# Abstraction




class Car:
    def __init__(self,color,model):
        self.c=color
        self.m=model
obj=Car('red','bmw')
print(obj.m)

class Dog:
    def bark(self):
        print('bhau bhau')
obj=Dog()
obj.bark()
class Bank:
    def __init__(self):
        self.__balance=500
    def get_balance(self):
        return self.__balance
b=Bank()
print(b.get_balance)



class Student:
    def __init__(self):
       print('adding new element in databases')
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student('ajay',98)
s2=Student('kishan',99)

print(s1.name,s1.marks)






class End:
    def __init__(self):
        pass
    @staticmethod
    def hello():
        print('hello world')
        
s1=End()
s1.hello()








# ABSTRACTION........................





class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print('car started....')
        
car1=Car()
car1.start()
        


        
        
# ENCAPSULATION...................

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    def debit(self,ammount):
        self.balance-=ammount
        print(ammount,"debited",self.get_balance())
        
    def credit(self,ammount):
        self.balance+=ammount
        print(ammount,"added",self.get_balance())
        
    def get_balance(self):
        return self.balance
        
    
acc1=Account(10000,12345)
acc1.debit(5000)
acc1.credit(12000)
        

# FUNCTIONS     



def f1():
    n = int(input("enter a number"))
    n = n**2

    print(n)


def f2():
    a = int(input("enter a number"))
    b = int(input("enter a number:-"))
    sum = a + b
    print(sum)


f1()
f1()
f2()








#  take something return nothing
def add(a,b,c):
    d=a*b*c
    print(d)
add(2,3,4)


# take nothing return something.


def add():
    print("enter two numbers")
    a = int(input())
    b = int(input())
    c = a + b
    print(c)
    return c


x = add()
print(x * 2)
x = x + 5
print(x)


def fact(a):
    i=1
    fact=1
    while(a>0):
        fact=fact*a
        a-=1
    print(fact)
    
    return(fact)
x=fact(5)
print(x*2)
x=x-60
print(x)




# take nothing return nothing


def add():
    print('enter two numbers')
    a=int(input())
    b=int(input())
    c=a+b
    print(c)
add()



# 1️⃣ Class aur Object (Basic)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

s1 = Student("Rahul", 20)
s1.show()


# 2️⃣ Constructor use
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Amit", 30000)
print(e1.name, e1.salary)



# 3️⃣ Method inside class
class Calculator:
    def add(self, a, b):
        return a + b

c = Calculator()
print(c.add(10, 20))

# 4️⃣ Inheritance (Parent → Child)
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()


# 5️⃣ Method Overriding
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()



# 6️⃣ Encapsulation (Private variable)
class Employee:
    def __init__(self, salary):
        self.__salary = salary   # private

    def get_salary(self):
        return self.__salary

e = Employee(40000)
print(e.get_salary())

# 7️⃣ Getter & Setter
class Person:
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

p = Person()
p.set_age(25)
print(p.get_age())



# 8️⃣ Polymorphism
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.sound()


# 9️⃣ Class Variable vs Instance Variable
class Employee:
    company = "TCS"   # class variable

    def __init__(self, name):
        self.name = name

e1 = Employee("Amit")
e2 = Employee("Rohit")

print(e1.company, e2.company)


# 🔟 Real-life Example (Bank Account)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(5000)
acc.deposit(2000)
acc.withdraw(3000)
acc.show_balance()



from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def interest_rate(self):
        pass

class SBI(Bank):
    def interest_rate(self):
        return "SBI Interest Rate: 6%"

class HDFC(Bank):
    def interest_rate(self):
        return "HDFC Interest Rate: 7%"

s = SBI()
h = HDFC()

print(s.interest_rate())
print(h.interest_rate())




class Father:
    def skill(self):
        print("Father: Driving")

class Mother:
    def skill(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
