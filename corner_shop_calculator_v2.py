# a dictionary to store the earnings for each food item.
earnings = {
    "Bubblegum": 202,
    "Ice cream": 2250,
    "Toffee": 118,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

# --------------------
# display earnings in a more structured way
print("**Shop Earnings**")
print("-----------------------")
total_income = 0
for item, amount in earnings.items():
    print(f"{item:<15}: ${amount}")
    total_income += amount
print("-----------------------")
print(f"**Total Income**: ${total_income}")

# --------------------
# calculate net income
print("\n--- Expenses ---")
try:
    staff_expenses = float(input("Enter staff expenses: "))
    other_expenses = float(input("Enter other expenses: "))
except ValueError:
    print("Invalid input. Please enter a numerical value for expenses.")
    staff_expenses = 0
    other_expenses = 0

net_income = total_income - staff_expenses - other_expenses
print(f"\n--- Results ---")
print(f"**Net Income**: ${net_income}")
