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

