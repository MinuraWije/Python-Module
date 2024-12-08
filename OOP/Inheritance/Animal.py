# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         pass        #Placeholder method, to be overrridden by subclasses

# class Dog(Animal):          #A constructor-less subclass will initialize it's superclass's constructor therefor we cannot  
#     def speak(self):        #call subclass as shown in line 15 as it is needed to include an argument while creating an object  
#         print ({self.name}, "says Woof")

# class Cat(Animal):
#     def speak(self):
#         print ({self.name}, "says Meow")

# #dog = Dog()
# dog = Dog("Roxy")
# print(dog.name)

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         pass   
# class Dog(Animal):
#     def __init__(self,name,color):      #When a custom constructor is called in a sub-class the super-class constructor is not called automatically.
#         self.color = color              
#         super().__init__(name)            #However we can call it explicitly as shown here.
#     def speak(self):        
#         print (self.name, "says Woof")

# class Cat(Animal):
#     def speak(self):
#         print (self.name, "says Meow")

# dog = Dog("Roxy","black")
# dog.speak()
# print(dog.name,"is",dog.color)

#Library management system
#You are tasked with creating a basic library management system using inheritance. Implement the following classes.
#   1. Base class- LibraryItem
#       Attributes-title(string), author(string), publication_year(int) 
#       Method - display_info() - print the details of the item
#   2. Derived class- Book   It inherits from LibraryItem
#       Additional attributes - genre(string),isbm(string)
#       Override display_info() - print the details including the genre and isbm
#   3. Derived class - Magazine     It inherits from LibraryItem
#       Additional attributes - issue(string) 
#       Override display_info() - print the details including the issue
#   Task - Create instances of each class(Book,Magazine) with appropriate values for their attributes
#   Call the diplay_info() method for each instance to test inherit inheritance and method overriding

class LibraryItem():
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(self.title," ",self.author," ",self.publication_year)
    
class Book(LibraryItem):
    def __init__(self,title,author,publication_year,genre,isbm):
        super().__init__(title,author,publication_year)
        self.genre = genre
        self.isbm = isbm

    def display_info(self):
        super().display_info()
        print(self.genre,self.isbm)

class Magazine(LibraryItem):
    def __init__(self,title,author,publication_year,issue):
        super().__init__(title,author,publication_year)
        self.issue = issue

    def display_info(self):
        super().display_info()
        print(self.issue)

book_1 = Book("Harry Potter","J.K. Rowling",2003,"Adventure","duq09w04309")
book_1.display_info()
magazine_1 = Magazine("Evo","Minura",2024,10)
magazine_1.display_info()