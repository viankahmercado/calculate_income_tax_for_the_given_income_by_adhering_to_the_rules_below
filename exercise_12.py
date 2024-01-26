# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 12:
# Calculate income tax for the given income by adhering to the rules below

# Expected Output: 
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

# assign income as variable
income = 19000
print("Given income:", income)

# if-else statment for condition
if income <= 10000:
    tax_to_pay = 0
elif income <= 20000:
    tax_to_pay = (income - 10000) * 10 / 100
else:
    tax_to_pay = 10000 * 10 / 100
    tax_to_pay += (income - 20000) * 20 / 100
# print the result
