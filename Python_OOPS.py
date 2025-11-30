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




