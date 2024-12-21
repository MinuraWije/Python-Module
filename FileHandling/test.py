# file_1 = open("FileHandling\myfile.txt","r")      #file_1 is an object 
# #file_content = file_1.read()                #default mode is read="r"
# #file_content = file_1.readline()             #readline()- reads the characters of the first line until "\n" is reached
# file_content = file_1.readlines()             #readlines()- Returns a list. Reads the characters of all lines until the end dividing it by "\n"           
# print(file_content,type(file_content))
# file_1.close()                               # It is a good programming practice to cloe the file after the operations given to it are complete.

#Different modes to open a file 
#r - Open a file for reading.(default)                      #The file has to exist 
#w - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
#x - Open a file for exclusive creation. If the file exists then the operation fails
#a - Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
#t - Open in text mode.(default)
#b - Open in binary mode

# 'with' statement for file handling ensure that files are properly closed after operations are complete, preventing issues like file locks,
# resource leaks or data corruptions.  

# with open("FileHandling\myfile.txt","r") as file:
#     content = file.read()
#     print(content)

# with open("FileHandling\my_file_1.txt","w") as file:
#     content = file.write("Hello World \nThis is our python class")
#     print(content)
    
# with open("FileHandling\my_file_1.txt","w") as file:
#     my_list = ["Hello world.\n","This is my python class"]
#     content = file.writelines(my_list)
#     print(content)

# with open("FileHandling\my_file_1.txt","a") as file:
#     file.write("\nWe are global citizens")

#Implement a simple contact mamagement system
# 1. Create a program that stores and manage contacts in a file named contacts.txt each contact entry should include name, phone nummber and email.
# 2. Features to implement- Add the new contact(Append the new contact to the file)
# 3. View all the contacts(Read and display all the contacts of the file)
# 4. Exit the program

def add_contact():
    with open("FileHandling\contacts.txt","a") as file:
        name = input("Enter new name : ")
        phone_number = input("Enter new phone number : ")
        email = input("Enter new email : ")
        file.write("\n"+name+","+phone_number+","+email)

def view_contacts():
    with open("FileHandling\contacts.txt","r") as file :
                contacts = file.readlines()
                for contact in contacts:
                    print(contact)

def exit_program():
    exit()

while True:
    print("Enter 1 to add a contact\nEnter 2 to display all contacts\nEnter 3 to exits")
    user_input = int(input("Enter your operation :"))
    match user_input:
        case 1:
            add_contact()
        case 2:
            view_contacts()
        case 3:
            exit_program()

