## input we need from the user
# total rent
#total food order and snaking
# electricity units spend
# charge per unit
           # <____________output__________>
#total amount or you have pay is

# Input section
rent = int(input('Enter your host/flat rent: '))
food = int(input('Enter the amount of food ordered: '))
electricity_spend = int(input('Enter the total electricity spent: '))
unit_price = int(input('Enter the charge per unit: '))
number_of_people = int(input('Enter the number of people living in the room: '))

# Calculate electricity bill
electricity_bill = electricity_spend * unit_price

# Calculate total cost
total_cost = rent + food + electricity_bill

# Calculate amount each person has to pay
amount_per_person = total_cost / number_of_people

# Output the result
print(f'Every person has to pay {amount_per_person:.2f}$')
