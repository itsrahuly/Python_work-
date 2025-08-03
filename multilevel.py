class animal:
    def speak(self):
        print("animal is speaking")

class dog(animal):
    def bark(self):
        print("Dog is barking")
class dogchild(dog):
    def eat(self):
        print("eating bread")


d=dogchild()
d.speak()
d.bark()
d.eat()
