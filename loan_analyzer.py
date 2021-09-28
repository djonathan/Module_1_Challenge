#! python
# coding: utf-8

import csv
from pathlib import Path

# Use a discount rate of %20 for all calculations
annual_discount_rate = 0.20

"""Part 1: Automate the Calculations.

    Use builtin functions to produce a loan summary

"""
loan_costs = [500, 600, 200, 1000, 450]

# Print the number of loans from the list
num_loans = len(loan_costs)

# Print the total value of the loans
sum_loans = sum(loan_costs)

# Print the average loan amount
avg_loan = sum_loans/num_loans

print(f"\nLoan details:\n\tTotal Loans: {num_loans}\n\tTotal value: {sum_loans}\n\t    Average: {avg_loan}")


"""Part 2: Analyze Loan Data.

    Analyze the loan to determine the investment evaluation.

    Given a loan in Python dictionary form, extract values and calculate the monthly form of Present Value:
        Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
"""

# Given the following loan data, calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = 0
remaining_months = 0
present_value = 0

# Extract and print future_value and remaining_months variables.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"\nFuture value: {future_value}")
print(f"Remaining months: {remaining_months}")

# Using a discount rate of 20%, calculate the monthly Present Value
present_value = future_value / (1 + (annual_discount_rate/12)) ** remaining_months
print(f"Present value: {present_value:.2f}")

# Suggest buying the loan if the calculated Present Value is greater than the loan cost
if present_value >= loan.get("loan_price"):
    print("This loan is worth the cost.")
else:
    print("This loan is too expensive.")


"""Part 3: Perform Financial Calculations.

    Perform financial calculations using functions.

"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Calculate and return Present Value
def calc_pv(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate / 12)) ** remaining_months
    return present_value

# Calculate the new_loan Present Value, using a pre-defined annual_discount_rate
present_value = calc_pv(new_loan.get("future_value"), new_loan.get("remaining_months"), annual_discount_rate)

print(f"\nThe present value of the loan is: {present_value:.2f}")


"""Part 4: Conditionally filter lists of loans.

    Loop through a series of loans, selecting only the inexpensive loans.

"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list 
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for item in loans:
    price = item.get("loan_price")
    if price <= 500:
        inexpensive_loans.append(item)

# Print the `inexpensive_loans` list
print(f"\nInexpensive loans:")
for item in inexpensive_loans:
    print(f"\t{item}")

"""Part 5: Save the results.

    Output this list of inexpensive loans to a csv file

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Create a CSV file with header and one row per loan entry
print("\nSaving these in inexpensive_loans.csv")
with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)

    for item in inexpensive_loans:
        csvwriter.writerow(item.values())

