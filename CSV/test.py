import csv

# csv_file_path = "CSV/customers-100.csv"

# with open(csv_file_path,"r",newline="") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader,type(csv_reader))
#     for row in csv_reader:
#         print(row,type(row))

# csv_file_path = "CSV/my_file.csv"
# field_names = ["Name","Age","City"]

# data =  [
#             {"Name":"Minura","Age":21,"City":"Moratuwa"},
#             {"Name":"Omesh","Age":22,"City":"Horana"}
#         ]

# with open(csv_file_path,"w",newline="")as csv_file:
#     csv_writer = csv.DictWriter(csv_file,fieldnames=field_names)
#     csv_writer.writeheader()
#     for row in data:
#         csv_writer.writerow(row)

# with open("CSV/my_file.csv","r") as file:
#     rows = csv.DictReader(file)
#     for row in rows:
#         print(row,type(row))

#You are tasked with creating a python program to manage a company's employee records stored in csv files. The program should read the employee details
# from a csv file, filter the records based on a condition and write the filter's records to a new csv files.
# Input file - employee.csv
# Contains the following fields,
#       EmployeeID, Name, Department, Salary
#       1, John, IT, 60000
#       2, Jane, HR, 55000
#       3, Brown, Finance, 70000
# Output file - high_salary_employee.csv
# You will create this file. It should contain records of employees whose salaries are above 57000. The fields should remain the same. 
# Tasks,
#       1. Read the input file - Use csv.reader to read employee.csv and display all the records on the console.abs
#       2. Filter the records - Identify employees with the salary>57000
#       3. Write the filtered records - Use csv.dictWriter to write the filtered records to a new file named high_salary_employees.csv. 

employee_csv = "CSV/employee.csv"
filtered_employee = []
with open("CSV/employee.csv","r",newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
        

with open("CSV/employee.csv","r",newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if int(row["Salary"])>57000:
            filtered_employee.append(row)

with open("CSV/high_salary_employees.csv","w",newline="") as csv_file:
    field_name = ["EmployeeID","Name","Department","Salary"]
    writer = csv.DictWriter(csv_file,fieldnames= field_name)
    writer.writeheader()
    writer.writerows(filtered_employee)
        
    