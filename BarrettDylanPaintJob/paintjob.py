# This program is designed to estimate the labor and supplies associated with a paint job.
import math

print('Paint job cost estimater.\n')

do_estimate = True
while (do_estimate):
    
    # Gather information about the paint job
    while (True): 
        try:
            square_feet = float(input("Enter the square feet of wall space: "))
            if (square_feet <= 0):
                print("Wall space must be greater than 0.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.") 
        else:
            break
    while (True):
        try:
            gallons_cost = float(input("What is the price of paint per gallon? "))
            if (gallons_cost <= 0):
                print("Price must be greater than 0.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
            
    # Calculate the gallons of paint required and labor hours.
    required_paint = square_feet/125
    labor_hours = required_paint*8
    
    # Calculate the paint and labor cost.
    paint_cost = math.ceil(required_paint)*gallons_cost
    labor_cost = labor_hours*42.5
    total_cost = paint_cost+labor_cost
    
    #Display supply and cost totals.
    
    print("Gallons of paint:", math.ceil(required_paint))
    print('Hours of labor:', format(labor_hours, ',.1f'))
    print('Paint cost: $',format(paint_cost, ',.2f'))
    print('Labor cost: $',format(labor_cost, ',.2f'))
    print('Total cost: $',format(total_cost, ',.2f'))
    
    another_estimate = input("Would you like to do another estimate? (y/n): ")
    if (another_estimate !="y"):
        do_estimate = False
    
    
    
    
        
                              

