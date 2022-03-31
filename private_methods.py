# Python program to 
# demonstrate private methods
  
# Creating a Base class 
class Base: 
  
    # Declaring public method
    def fun(self):
        print("Public method")
  
    # Declaring private method
    def __fun(self):
        print("Private method")
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self) 
        self.__dick = 'd'
          
    def __derived_fun(self):
        print("Derived Private Method!")

    def call_public(self):
          
        # Calling public method of base class
        print("\nInside derived class")
        self.fun()
          
    def call_private(self):
          
        # Calling private method of base class
        #self.__fun()

        #
        self.__derived_fun()
  
# Driver code 
obj1 = Base()
  
# Calling public method
obj1.fun()
  
obj2 = Derived()
obj2.call_public()

obj2._Derived__derived_fun()

print(obj2._Derived__dick)
  
# obj1.__fun() 
# raise an AttributeError 
  
obj2.call_private() 
# will also raise an AttributeError


# Python program to 
# demonstrate private methods
   
# # Creating a class 
# class A: 
   
#     # Declaring public method
#     def fun(self):
#         print("Public method")
   
#     # Declaring private method
#     def __fun(self):
#         print("Private method")
      
#     # Calling private method via
#     # another method
#     def Help(self):
#         self.fun()
#         self.__fun()
          
# # Driver's code
# obj = A()
# obj.Help()
# obj.fun()
# obj.__fun()