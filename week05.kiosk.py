# ISHS CAFE
# 아메리카노 1500, 라떼 2500

beverage = ["Americano",  "Latte"]
prices = [1500, 2500]
total_price = 0

while True:
    menu = input("1) Americano 2) Latte 3) End order :")
    if menu == '3':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        print("You ordered Americano. The price is 1500 won")
        total_price = total_price + prices[0]
    elif menu == '2':
        print("You ordered Latte. The price is 2500 won")
        total_price = total_price + prices[1]
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu")

print(f"Tht total amount is {total_price} won.")