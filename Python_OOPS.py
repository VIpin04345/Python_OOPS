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


