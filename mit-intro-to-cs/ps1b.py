###############################################################################
#       9 March 2021
#       Saving with a raise
#
#       Test Case 1
#       >>>
#       Enter your starting annual salary: 120000
#       Enter the percent of your salary to save, as a decimal: .05
#       Enter the cost of your dream home: 500000
#       Enter the semi­annual raise, as a decimal: .03
#       Number of months: 142
#       >>>
#
#       Test Case 2
#       >>>
#       Enter your starting annual salary: 80000
#       Enter the percent of your salary to save, as a decimal: .1
#       Enter the cost of your dream home: 800000
#       Enter the semi­annual raise, as a decimal: .03
#       Number of months: 159
#       >>>
#
#       Test Case 3
#       >>>
#       Enter your starting annual salary: 75000
#       Enter the percent of your salary to save, as a decimal: .05
#       Enter the cost of your dream home: 1500000
#       Enter the semi­annual raise, as a decimal: .05
#       Number of months: 261
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
semi_annual_raise = float( input('Enter the semi­annual raise, as a decimal: ') )

down_payment = portion_down_payment * total_cost

month_counter = 0
while current_savings <= down_payment:
    monthly_savings = ( annual_salary / 12 ) * portion_saved
    current_savings += current_savings*r_monthly + monthly_savings
    month_counter +=1
    if month_counter % 6 == 0:
        #print( month_counter, int(annual_salary) )
        annual_salary += annual_salary * semi_annual_raise

print('Number of months: ', month_counter)
print('Number of years: ', float( month_counter )/ 12)
