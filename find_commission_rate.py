# Define the base salary
base_salary = 5000

# Define the target annual income
target_income = 30000

# Calculate the commission rate based on the sales amount
def calculate_commission_rate(sales_amount):
    if sales_amount <= 5000:
        return 0.08
    elif sales_amount <= 10000:
        return 0.1
    else:
        return 0.12


# Calculate the minimum amount of sales needed to earn the target income
# Start with the base salary and increment the sales amount by $1 until the target income is reached
sales_amount = 0
total_income = base_salary
while total_income < target_income:
    sales_amount += 1
    commission_rate = calculate_commission_rate(sales_amount)
    commission = sales_amount * commission_rate
    total_income = base_salary + commission

# Print the minimum amount of sales needed
print(
    f"To earn ${target_income:,}, you need to generate at least ${sales_amount:,} in sales.")