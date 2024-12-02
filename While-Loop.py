# m=5
# i=0
# while i<m:
#     print(i, end =" ")          # end - specifies what to be printed at the end of the given line
#     i += 1
# print("End")

# x = int(input("Enter your number : "))
# num = 0
# while num<x:
#     if num==10:
#         break
#     elif num%2==0:
#         print(num)
#     num += 1


# sum = 0

# while True:
#     x = int(input("Enter a number : "))
#     if x==0:
#         break
#     else:
#         sum+=x
# print("The sum is ",sum)

my_list = [3,8,15,10,9,7,14]
num = 0
for x in my_list:
    if x%2==0:
        continue
    print(x)