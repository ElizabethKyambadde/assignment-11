# Personal Finance Planner
# This program helps users plan their monthly budget.

def leftover_income(income, expenses, savings_goal):
    return income - expenses - savings_goal

try:
    income = float(input("Monthly Income: "))
    expenses = float(input("Fixed Expenses: "))
    savings_goal = float(input("Savings Goal: "))

    leftover = leftover_income(income, expenses, savings_goal)

    if leftover > 0:
        print("You can meet your savings goal. Leftover money:", leftover)
    elif leftover == 0:
        print("You will meet your savings goal but have no extra money.")
    else:
        print("You need to reduce spending by", abs(leftover))

        # suggestions
        if abs(leftover) > 500:
            print("Advice: Reduce entertainment and eating out.")
        elif abs(leftover) > 200:
            print("Advice: Cut down on shopping.")
        else:
            print("Advice: Reduce small daily expenses.")

except ValueError:
    print("Please enter numbers only.")
