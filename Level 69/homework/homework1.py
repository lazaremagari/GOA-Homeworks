# 1) შექმენით ფუნქცია რომელიც მიიღებს ადამიანის სახელს და შემდეგ დაუპრინტავს მისასალმებელ წერილს

user_name = input("enter your name here -> ")

def greetings(name):
    return "hello " + name
print(greetings(user_name))