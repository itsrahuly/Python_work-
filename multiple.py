class mother:
    def mother(self):
        print("i am mother")
class father:
    def father(self):
        print("i am father")
        
class son(mother,father):
    def parent(self):
        print("i am son of my parent")


s1=son()
s1.mother()
s1.father()
s1.parent()
