print("select from here:\n1.well\n2.shears\n3.paper")
numbers = ["1", "2", "3"]
player1 = input("player 1 -> ")
player2 = input("player 2 -> ")
if player1 not in numbers and player2 not in numbers:
    print("you have ran out from nombers")
else:
    if player1 == player2:
        print("it's tie")
    elif player1 == "1" and player2 == "2":
        print("player1 wins🥳")
    elif player1 == "2" and player2 == "3":
        print("player1 wins🥳")
    elif player1 == "3" and player2 == "1":
        print("player1 wins🥳")
    else:
        print("player2 wins🥳")