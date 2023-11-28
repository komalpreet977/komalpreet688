qtr = 25
penny = 1
nickel = 5
dime = 10
Pennies_In_Dollar = 100

def count_a_dollar():
    a = int(input("Enter the number of quarters: "))
    b = int(input("Enter the number of pennies: "))
    c = int(input("Enter the number of nickels: "))
    d = int(input("Enter the number of dimes: "))

    cal = (a * qtr) + (b * penny) + (c * nickel) + (d * dime)

    total_dollars = cal / Pennies_In_Dollar

    if total_dollars > 1:
        print("Sorry, the amount you entered is more than one dollar.")
    elif total_dollars < 1:
        print("Sorry, the amount you entered is less than one dollar.")
    else:
        print("Congratulations! The amount you entered was exactly one dollar, and you win the game!")

count_a_dollar()
