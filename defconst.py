class car:
    def __init__(self):
     print("i am constructor")
     self.color=input("enter a color:")
     self.model="FORD"

    def display(self):
        print("i am normal function in class")
    
c=car()
print("color is:",c.color)
print("Model is:",c.model)
c.display()
    