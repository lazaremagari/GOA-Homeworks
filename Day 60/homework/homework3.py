def rame(num1, num2):
    if num1 < num2:
        return "num1 aris umciresi"
    elif num1 == num2:
        return "arcerti ar aris umciresi"
    else:
        return "num2 aris umciresi"
    
print(rame(int(input("enter first number: ")), int(input("enter second number: "))))