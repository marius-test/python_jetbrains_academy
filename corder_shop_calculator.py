print("Earned amount:")
print("Bubblegum: $202")
print("Ice cream: $2250")
print("Toffee: $118")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")
print("Income: $5405.0")

income = 5405.0

print("Staff expenses:")
staff_expenses = float(input())

print("Other expenses:")
other_expenses = float(input())

net_income = income - staff_expenses - other_expenses
print(f"Net income: ${net_income}")
