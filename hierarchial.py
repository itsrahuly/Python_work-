class parent:
    def fun1(self):
        print("parent class")

class child1(parent):
    def fun2(self):
        print("child1 class")

class child2(parent):
    def fun3(self):
        print("Child 2 is class function")

obj=child1()
obj1=child2()
obj.fun1()
obj.fun2()

obj1.fun1()
obj1.fun3()
