# class MyClass:
#     def __init__(self,protected_var,private_var):
#         self._protected_var = protected_var
#         self.__private_var = private_var

#     def _protected_method(self):
#         print("Protected method")
    
#     def __private_method(self):
#         print("Private method")

# my_obj = MyClass("test1","test2")
# print(my_obj._protected_var)            #Protected variable can be accessed from outside but is not encouraged.
# print(my_obj.__private_var)             #Private variable cannot be accessed by outside.
# my_obj._protected_method()              #Protected method can be accessed from outside but is not encouraged.
# my_obj.__private_method()               #Private method cannot be accessed from outside.


# class Example:
#     def __init__(self):
#         self.__data = "Encapsulated Data"

#     def get_value(self):
#         print("Value of details",self.__data)

#     def set_value(self,new_data):
#         self.__data = new_data

# my_example = Example()
# my_example.get_value()
# my_example.set_value("New Data")
# my_example.get_value()

#Implement a QuadraticEquation class that represent a quadratic equation of the form ax^2+bx+c=0. The class should have attributes,
#   private attributes- __a,__b,__c to store the coefficient of the quadratic equation
#   methods - A constructor to initialize the coefficient of __a,__b,__c
#   private method - __descriminant() that calculates and returns the descriminant(D=b^2-4ac)
#   public method - find_roots() and use the private __discriminant() method. Return the root of the quadratic equation 
#   if D=0 ,now 1 real root
#   if D>0 , 2 disctinct real roots
#   if D<0, 2 complex roots

class QuadraticEquation():
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c

    def __descriminant(self):
        return self.__b**2-4*self.__a*self.__c

    def find_roots(d):
        if(d==0):
            root=(-(self.__b)/2*self.__a)
            print("The root is",root)
        elif(d>0):
            root1=((-self.__b+d**(1/2))/2*self.__a)
            root2=((-self.__b-d**(1/2))/2*self.__a)
            print("Two roots are",root1,root2) 
        else:
            print("There's 2 complex roots")

equation1 = QuadraticEquation(1,-5,6)
equation1.find_roots()