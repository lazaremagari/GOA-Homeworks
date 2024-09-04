def number(num):
    if num % 2 == 0:
        return "it's even"
    else:
        return "its odd"
print(number(int(input("enter number here -> "))))