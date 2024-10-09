# 2) შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია შემდეგ გამოიტანეთ ამ ყველა რიცხვის ჯამი

broskie_list = [2, 6, 3, 8, 5, 9]

def sum_of_list(list):
    list_sum = 0
    for i in range(len(list)):
        list_sum = list_sum + list[i]
    print(list_sum)

sum_of_list(broskie_list)