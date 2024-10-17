# Nexabet
# 9/26/20240
# P1HW2
# For this assignment you will create a program that does some basic math about expenses
# Ask user for info
print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
print()
travel_destination = (input("Enter Travel Destination: "))
print()
Gas_expense = int(input("How much do you think you will spend on gas?: "))
print()
accomodation_expense = int(input("Approximately, how much will you need for accomodation/hotel?: "))
print()
food_expense = int(input("Last, how much do you need for food?: "))
Total_expense = int(Gas_expense + accomodation_expense + food_expense)
# Calculate remaining balance
remaining_balance = (budget - Total_expense)
# Display expenses
print()
print("-------------Travel Expenses------------")
print(f"{'Location:' :<20}{travel_destination}")
print(f"{'Initial Budget:' :<20}${budget:,.2f}")
print(f"{'Fuel:' :<20}${Gas_expense:,.2f}")
print(f"{'Accomodation:' :<20}${accomodation_expense:,.2f}")
print(f"{'Food:' :<20}${food_expense:,.2f}")
print("-" * 40)
print(f"{'Remaining Balance:' :<20}${remaining_balance:,.2f}")


