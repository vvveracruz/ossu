###############################################################################
#
#       27 March 2021
#
#       Problem Set 1 Part C:
#       Finding the right amount to save away 
#
#       -----------------------------------------------------------------------
#
#       Using bisection search to find the ideal savings rate over an amount 
#       of months to reach a savings goal
#
#       -----------------------------------------------------------------------
#     
#       Test Case 1 
#       >>>  
#       Enter the starting salary: 150000
#       Best savings rate: 0.4411  
#       Steps in bisection search: 12 
#       >>>
#       
#       Test Case 2 
#       >>>  
#       Enter the starting salary: 300000
#       Best savings rate: 0.2206 
#       Steps in bisection search: 9 
#       >>>
#
#       Test Case 3 
#       >>>  
#       Enter the starting salary: 10000
#       It is not possible to pay the down payment in three years.
#       >>>
#
###############################################################################

import time

#   CONSTANTS
#   ---------
home_price_usd = 1000000
semi_annual_raise_rate = 0.07
required_down_payment_rate = 0.25
goal_time_period_months = 36
initial_savings = 0
annual_savings_return_rate = 0.04
monthly_savings_return_rate = annual_savings_return_rate / 12

initial_annual_salary = float( input( 'Enter the starting salary: '))
# initial_annual_salary = 150000

epsilon = 100
savings_goal = home_price_usd * required_down_payment_rate


def get_savings_accrued( savings_rate ):
    '''
    '''
    # print( 'Enter accrued savings calculator' )
    current_savings = initial_savings
    current_annual_salary = initial_annual_salary

    month_counter = 0
    for month_counter in range(0, goal_time_period_months ):
        monthly_savings = ( current_annual_salary / 12 ) * savings_rate
        current_savings += current_savings * monthly_savings_return_rate + monthly_savings
        month_counter += 1
        if month_counter % 6 == 0:
            current_annual_salary += current_annual_salary * semi_annual_raise_rate
    return current_savings
    

#   BISECTION SEARCH
#   --------- ------
guess_counter = 1
low = 0
high = 10000
guess = ( high + low ) / 2

savings_accrued = 0
while abs( savings_goal - savings_accrued ) >= epsilon and low != high:
    # print('Guess number:', guess_counter)
    # print('High:', high, 'Low:', low)
    guess_counter += 1
    savings_accrued = get_savings_accrued( guess / 10000 )
    if savings_accrued < savings_goal:
        low = guess
    else:
        high = guess
    # time.sleep(1)
    guess = ( high + low ) / 2

if low == high:
    print('It is not possible to pay the downpayment in', goal_time_period_months / 12, 'years')
else:
    best_savings_rate = guess /  10000
    print( 'Best savings rate:', best_savings_rate )
    print( 'Steps in bisection search:', guess_counter )