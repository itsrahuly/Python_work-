class info:
    name=input("enter a name:")
    age=int(input("enter a age"))
    Class=input("enter a class")
    city=input("Enter a city:")

    def person(self):
        print("your name is:",self.name)
        print("your age is:",self.age)
    
    def subinfo(self):
        print("your class is:",self.Class)
        print("your city is:",self.city)


i=info()
print(i.person())
print(i.subinfo())
