def guess(num):
    user_guess = int(input("guess the number -> "))
    while user_guess != num:
        user_guess = int(input("incorrect try again -> "))
    print("Congrats!!! You wiiiiin 🥳🥳🥳🥳")