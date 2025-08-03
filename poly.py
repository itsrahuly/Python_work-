class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class plane:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")

c1=car("ford","mustang")
b1=Boat("tata","touring ")
p1=plane("boeing","tor")


for x in (c1,b1,p1):
    x.move()

