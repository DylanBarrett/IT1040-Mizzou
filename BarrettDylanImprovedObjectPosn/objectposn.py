# Explain the purpose of the program
print("This program is designed to calculate an object's final position.\n")

do_calculation = True
while (do_calculation):

    # Gather information about the object from the user
    while (True):
        try:
            initial_position = float(input("Enter the object's initial position: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
    while (True):
        try:
            initial_velocity = float(input("Enter the object's initial velocity: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
    while (True):
        try:
            acceleration = float(input("Enter the object's acceleration: "))
        except ValueError:
            print("The Value you entered is invalid. Only numerical values are valid.")
        else:
            break
    while (True):
        try:
            time = float(input("Enter the time that has elapsed: "))
            if (time < 0):
                print("Nevative elapsed time is not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    # Calculue the final position
    final_position = initial_position+initial_velocity*time+1/2*acceleration*time**2


    # Display the final position
    print("\nThe object's final position is", final_position)



    another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if (another_calculation !="y"): 
        do_calculation = False
        
                               
