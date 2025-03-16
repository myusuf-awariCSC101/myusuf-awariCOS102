
# calculateing simple interest and the total amount
def simple_interest(P, R, T):
    A = P * (1 + (R / 100) * T)
    return A

# calculating compound interest and the total amount
def compound_interest(P, R, T, n):
    A = P * (1 + R / n) ** (n * T)
    return A

# calculating annuity plan and the total amount
def annuity_plan(PMT, R, T, n):
    A = PMT * ((1 + (R / n)**(n * T) - 1) / (R / n))
    return A

# let the user try it out
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Interest Rate: "))
T = float(input("Enter Time Period: "))
n = int(input("Enter Number of Compounding Periods per Year: "))
PMT = float(input("Enter Annuity Payment (if applicable): "))


print("Simple Interest:", simple_interest(P, R, T))
print("Compound Interest:", compound_interest(P, R, T, n))
print("Annuity Plan:", annuity_plan(PMT, R, T, n))



