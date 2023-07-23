"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONU_RATE_LOW = 0.1
BONU_RATE_HEIGH = 0.15

sales = float(input("Enter sales $"))
while sales >= 0:
    if sales < 1000:
        bonu = sales * BONU_RATE_HEIGH
    else:
        bonu = sales * BONU_RATE_LOW
    print(f"Bonu is: {bonu}$")
    sales = float(input("Enter sales: $"))

