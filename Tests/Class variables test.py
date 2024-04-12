class MyClass():
    def __init__(self):
        self.var1 = 8  # use self to make var1 an instance variable
    
    def my_method(self):
        self.var1 = 10  # use self to access the instance variable

object1 = MyClass()
print(object1.var1)  # no parentheses after object1
object1.var1 = 20
print(object1.var1)  # no parentheses after object1