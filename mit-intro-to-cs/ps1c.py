###############################################################################
#
#       9 March 2021
#       Finding the right amount to save
#
###############################################################################

#   constants
portion_down_payment = 0.25
current_savings = 0
r_annual = 0.04
r_monthly = 0.04 / 12
semi_annual_raise = .07
total_cost = 1000000
down_payment = portion_down_payment * total_cost
goal_months = 36
var = 100

#   user input
annual_salary = float( input('Enter your annual salary: ') )
portion_saved  = float( input('Enter the percent of your salary to save, as a decimal: ') )


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
