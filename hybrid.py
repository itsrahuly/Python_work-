class school:
    def func1(self):
        print("this function is in school")

class studnet(school):
    def func2(self):
        print("this function is in student1")

class studnet2(school):
    def func3(self):
        print("this function is in student2")

class stud(studnet,school):
    def func4(self):
        print("this function is in student3")

obj=stud()
obj.func1()
obj.func2()
