#1) შექმენით ფუნქცია, სადაც გადაცემთ 5 საგნის ნიშნებს(სკოლის ნიშნებზეა საუბარი), პარამეტრად, 
# თქვენი მიზანია რომ გამოიანგარიშოთ ამ რიცხვების საშუალო არითმეტიკული.

def sashualo(pirveli, meore, mesame, meotxe, mexute):
    print((pirveli + meore + mesame + meotxe + mexute) / 5)

sashualo(int(input("enter first mark -> ")), int(input("enter second mark -> ")), int(input("enter third mark -> ")), int(input("enter fourth mark -> ")), int(input("enter fifth mark -> ")),)