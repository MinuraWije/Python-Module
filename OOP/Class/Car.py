# class Car:
#     category = "motor-vehicle"      #attribute      class attribute

# new_car = Car()             #creating an object 
# print(new_car.category)     

#The Python self
#It is a conventionally used name for the 1st parameter of instance methods in a class. It represents the instance of the class itself.

# class Car:
#     category = "motor-vehicle"

#     def display(self):
#         print("This is a display function.")

# new_car = Car()
# print(new_car.display())


#__init__ method
#This is crucial in object initialization. You define this method within a class to specify how object attributes should be set up 
# when the object is created.

# class Car:
#     category = "motor-vehicle"

#     def __init__(self,model,color):
#         self.model = model      #model and car on the left is instance attribute
#         self.color = color

# class Car:
#     def __init__(self,model,color):
#         self.model = model
#         self.color = color

#     def display(self):
#         print(self.model,self.color)

# new_car = Car("Ferrari","red")
# new_car.display()
# print(self.model)
# print(self.color)


# class Car:
#     category = "motor-vehicle"
#     def __init__(self,model,color):
#         self.model = model
#         self.color = color

#     def display(self):
#         print(self.model,self.color)
    
#     def update(self,new_model,new_color):
#         self.model = new_model
#         self.color = new_color
#         print(self.model)
#         print(self.color)


# Car("Ferrari", "red").update("Toyota","red")     #Class attributes can be called without creating an object. But instance attributes cannot be called 
# new_car.display()                   #directly without creating an object
# # new_car.update("Audi","black")
# new_car.display()
# print(new_car.category)

#Create a class name BankAccount() with the following,
#   an attribute account_holder to store the name of the account holder
#   an attribute balance to store the account balance,initalized to=0
#Add the following methods to the class,
#   deposit(amount)         adds the given amount to the balance
#   withdraw(amount)        subtract the given amount from the balance if sufficient funds exist, otherwise print an error msg
#   display_balance()       prints the current balance
#Write a small script to demonstrate the following 
#   create an object of the bank account class 
#   perform a few deposit and withdrawal operations
#   display the balance after each operation

class BankAccount():
    
    def __init__(self,holder):
        self.holder = holder
        self.balance = 0
    
    def deposit(self,amount):
        if(amount>0):
            self.balance +=amount
            self.display_balance(self.balance)
        else:
            print("Cannot deposit a negative value")

    def withdraw(self,amount):
        if (self.balance>amount):
            self.balance -= amount
            self.display_balance(self.balance)
        else:
            print("Insufficient funds.")
    
    def display_balance(self,balance):
        print(self.holder," : ",self.balance)

new_holder = BankAccount("Minura")
new_holder.deposit(50000)
new_holder.deposit(-1000)
new_holder.withdraw(5000)
new_holder.withdraw(50000)
new_holder.deposit(15000)