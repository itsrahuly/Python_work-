class car:
    def __init__(self,color, model,price):
        self.x=color
        self.y=model
        self.z=price

    def display(self):
        print("i am normal function in a class")
        

c=car("black","ford","20000")

print("color is:",c.x)
print("model is:",c.y)
print("price is:",c.z)

     
