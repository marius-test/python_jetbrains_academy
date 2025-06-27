import math
import sys


# calculate principal amount using formula P = A / (i*(1+i)^n/((1+i)^n-1))
# where A is annuity payment
# i is nominal interest
# n is number of payments
def calculate_principal(A, i, n):
    den = (i * pow(1 + i, n)) / (pow(1 + i, n) - 1)
    P = A / den
    overpayment = (A * n) - P
    print(f"Your credit principal = {math.ceil(P)}!")
    print(f"Overpayment = {math.ceil(overpayment)}")


# calculate annuity payment using formula A = p*(i*(1+i)^n/((1+i)^n - 1)))
# where P is loan principal
# i is nominal interest
# n is number of payments
def calculate_annuity(n, i, P):
    A = P * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    A = math.ceil(A)
    overpayment = (A * n) - P
    print(f"Your annuity payment = {A}!")
    print(f"Overpayment = {math.ceil(overpayment)}")


# calculate no of payments using formula n = log1+i(A/(A-(i*p)))
# where A is annuity payment
# i is nominal interest
# p is loan principal
def calculate_months(P, A, i):
    n = math.log(A / (A - i * P), 1 + i)
    n = math.ceil(n)
    years = n // 12
    month = n - years * 12
    year_str = ""
    month_str = ""
    if month > 1:
        month_str = str(month) + " months"
    elif month == 1:
        month_str = str(month) + " month"
    if years > 1:
        year_str = str(years) + " years"
    elif years == 1:
        year_str = str(years) + " year"
    if month != 0 and years != 0:
        print(f"You need {year_str} and {month_str} to repay this credit!")
    else:
        print(f"You need {year_str}{month_str} to repay this credit!")
    overpayment = (A * n) - P
    print(f"Overpayment = {math.ceil(overpayment)}")


# calculate differential payment using formula Dm = P/n + i*(P-(p*(m-1)/n))
# where P is loan principal
# n is number of payments
# i is nominal interest rate
# m is current repayment month
def calculate_diff(P, n, i):
    sum = 0
    for j in range(1, n + 1):
        sec = P * (j - 1) / n
        sec = P - sec
        D = P / n + i * sec
        D = math.ceil(D)
        sum += D
        print(f"Month {j}: paid out {D}")
    overpayment = sum - P
    print(f"Overpayment = {overpayment}")


args = sys.argv
# args = ["","--type=diff", "--principal=1000000", "--periods=10", "--interest=10"]
key = []
value = []
for i in args[1:]:
    key1, value1 = i.replace("--", "").split("=")
    key.append(key1)
    value.append(value1)


# check for loan type and required parameters
if "annuity" not in value and "diff" not in value:
    print("Incorrect parameters")
elif "interest" not in key:
    print("Incorrect parameters")
elif "payment" in key and "diff" in value:
    print("Incorrect parameters")
else:
    principal_f, payment_f, periods_f = 1, 1, 1
    if "type" in key:
        type = value[key.index("type")]
    if "principal" in key:
        principal = float(value[key.index("principal")])
        if principal < 0:
            print("Incorrect parameters")
    else:
        principal_f = 0
    if "interest" in key:
        interest = float(value[key.index("interest")])
        if interest < 0:
            print("Incorrect parameters")
        nominal_interest = interest / (12 * 100)
    if "payment" in key:
        payment = float(value[key.index("payment")])
        if payment < 0:
            print("Incorrect parameters")
    else:
        payment_f = 0
    if "periods" in key:
        periods = int(value[key.index("periods")])
        if periods < 0:
            print("Incorrect parameters")
    else:
        periods_f = 0
    if type == "diff":
        calculate_diff(principal, periods, nominal_interest)
    else:
        if principal_f == 0:
            calculate_principal(payment, nominal_interest, periods)
        elif payment_f == 0:
            calculate_annuity(periods, nominal_interest, principal)
        elif periods_f == 0:
            calculate_months(principal, payment, nominal_interest)
