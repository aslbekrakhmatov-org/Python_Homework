def invest(amount, rate, years):
    for x in range(1, years+1):
        amount+=amount*(rate/100)
        print(f"Year {x}: {round(amount, 2)}")

user_amount = int(input("Enter the amount of your investment: "))
user_rate = float(input("Enter the percentage of the rate: "))
user_year = int(input("Enter the number of years: "))
invest(user_amount, user_rate, user_year)