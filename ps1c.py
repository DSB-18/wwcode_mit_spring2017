# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:07:08 2017

@author: Дима
"""

annual_salary=int(input("Enter the starting salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04 
low = 0
high = 10000
num_guesses = 0
if annual_salary * 3 < portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
while abs(portion_down_payment - current_savings) >= 100:
    current_savings = 0
    monthly_salary = annual_salary / 12
    portion_s = (high + low) / 2
    for i in range (36):
        if (i + 1) % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
       
        monthly_savings = monthly_salary * (portion_s / 10000)
        current_savings = current_savings + current_savings * r / 12 + monthly_savings
        
    if current_savings - portion_down_payment < 0:
        low = portion_s
    else:
        high = portion_s
    num_guesses += 1 

if portion_s > 6000:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: ", round(portion_s/10000, 4))
    print("Steps in bisection search: ", num_guesses)