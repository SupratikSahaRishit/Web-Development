class Student:
    __schoolName = 'XYZ School'

    def __init__(self, name, age):
        self._name = name


    def __display(self):
        print("This is private method .")


std = Student("Bill" , 25)
print(std.__schoolName)