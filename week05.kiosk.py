# ISHS CAFE
# 아메리카노 1500, 라떼 2500

beverage = ["Americano",  "Latte"]
prices = [1500, 2500]

while True:
    menu = int(input("1) Americano 2) Latte 3) End order :"))
    if menu == 3:
        print("Exit Program")
        break
    elif menu == 1:
        print("You ordered Americano. The price is 1500 won")
    elif menu == 2:
        print("You ordered Latte. The price is 2500 won")