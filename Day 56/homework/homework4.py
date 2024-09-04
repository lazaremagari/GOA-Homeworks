def calculator(num1, num2, operator):
    print(eval(str(num1) + operator + str(num2)))


calculator(int(input("enter first number -> ")), int(input("enter second number -> ")), input("enter operator -> "))