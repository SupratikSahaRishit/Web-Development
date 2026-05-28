class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self._c = "GeeksforGeeks"

class Derived(Base):
    def __init__(self):



        Base.__init__(self)
        print("Calling private number of base class :")
        print(self._c)


obj1 = Base()
print(obj1.a)
   