# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:07:08 2017

@author: Дима
"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0

while current_savings < portion_down_payment:
    current_savings += current_savings * r / 12 + annual_salary / 12 * portion_saved
    months += 1
          
print("Number of months: ", months)