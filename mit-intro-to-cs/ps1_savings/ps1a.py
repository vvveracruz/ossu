###############################################################################
#       9 March 2021
#       Saving for a house
#
#       Test Case 1
#       >>>
#       Enter your annual salary: 120000
#       Enter the percent of your salary to save, as a decimal: .10
#       Enter the cost of your dream home: 1000000
#       Number of months: 183
#       >>>
#
#       Test Case 2
#       >>>
#       Enter your annual salary: 80000
#       Enter the percent of your salary to save, as a decimal: .15
#       Enter the cost of your dream home: 500000
#       Number of months: 105
#       >>>
#
###############################################################################

#   constants
portion_down_payment = 0.25
current_savings = 0
r_annual = 0.04
r_monthly = 0.04 / 12

#   user input
annual_salary = float( input('Enter your annual salary: ') )
portion_saved  = float( input('Enter the percent of your salary to save, as a decimal: ') )
total_cost = float( input('Enter the cost of your dream home: ') )

down_payment = portion_down_payment * total_cost
monthly_savings = ( annual_salary / 12 ) * portion_saved

month_counter = 0
while current_savings < down_payment:
    current_savings += current_savings*r_monthly + monthly_savings
    month_counter +=1

print('Number of months: ', month_counter)
print('Number of years: ', float( month_counter )/ 12)
