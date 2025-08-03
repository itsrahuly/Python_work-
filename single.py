class parent:
    def pfun(self):
        print("parent class")

class child(parent):
    def fun(self):
        print("child class")

c1=child()
c1.pfun()
c1.fun()
