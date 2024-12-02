# def find_factorial(n):
#     factor=1
#     if n==0:
#         return 1
#     while not n==0:         #for n in range (1,n+1)
#         factor *= n
#         n = n-1
#     return factor
# print(find_factorial(0))

# def rec_factorial(n):                       #The maximum depth of recursion is 1000
#     if n==0 or n==1:
#         return 1
#     else:
#         return(n*rec_factorial(n-1))
# print(rec_factorial(1000))

#Using recursive function return the sum of the elements of a list

my_list = [4,8,5,9,16]

def rec(x):
    if not x:
        print("List is empty")
    else:
        return (x[0] + rec(x[1:]))
    
print(rec(my_list))