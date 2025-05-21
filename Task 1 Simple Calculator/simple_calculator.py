#Calculator:
a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
operator=input("Enter operator:")
if operator=="+":
    print(f"Addition of two numbers is {a+b}")
elif operator=="-":
    print(f"Substraction of two numbers is {a-b}")
elif operator=="*":
    print(f"Multiplication of two numbers is {a*b}")
elif operator=="+":
    print(f"Division of two numbers is {a/b}")
else:
    print(f"Given operator is invalid:{operator}")