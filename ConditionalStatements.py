# a=56
# if a<0:
#     print("This is a negative number")
# elif a>0:
#     print("This is a positive number")
# else:
#     print("This is zero")

# marks = int(input("Enter your marks :"))
# if marks>100 or marks<0:
#     print("Invalid marks")
# elif 85<=marks:
#     print("A")
# elif 75<=marks:
#     print("B")
# elif 65<=marks:
#     print("C")
# elif 55<=marks:
#     print("D")
# else:
#     print("F")

a=10
b=1
c=8

if a>b and a>c:
    print("a")
elif b>a and b>c:
    print("b")
elif c>b and c>a:
    print("c")
elif a==b and a>c:
    print("a and b")
elif a==b and c>a:
    print("c")
elif c==b and a>c:
    print("a")
elif c==b and c>a:
    print("b and c")
elif a==c and a>b:
    print("a and c")
elif a==c and b>a:
    print("b")
else:
    print("a,b and c ")


