# Trip Planner
# ------------
# The following program helps to create a travel itinerary


# Import modules
import destinations
import currency


def main():
    # Print a welcome message
    print_welcome()


    # Show destinations
    destinations.print_options()
    
    # Pick destination
    choice = destinations.get_choice()
    
    # Get destination info
    destination, euro_rate = destinations.get_info(choice)


    # Calculate currency exchange
    dollar_rate = currency.convert_euros_to_dollars(euro_rate)

    # Determine length of stay
    while True:
        try:
            length_of_stay = int(input("And how many days will you be staying in " + destination + "? "))
            # Check for non-positive input
            if (length_of_stay <= 0):
                print("Please enter a positive number of days.")
                continue  
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    # Calculate cost
    cost = dollar_rate * length_of_stay


    # Save itinerary
    try:
        save_itinerary(destination, length_of_stay, cost)
        
    # Catch file errors
    except:
        print("Error: the itinerary could not be saved.")
        
    # Print confirmation
    else:
        print("\nYour trip to", destination, "has been booked!")





def print_welcome():
    # Print a welcome message
    print("---------------------------")
    print("Welcome to the Trip Planner")
    print("---------------------------")
    print()


def save_itinerary(destination, length_of_stay, cost):
    # Itinerary File Name
    file_name = 'itinerary.txt'
    
    # Create a new file
    itinerary_file = open(file_name, 'w')

    # Write trip information
    itinerary_file.write('Trip Itinerary\n')
    itinerary_file.write('--------------\n')
    itinerary_file.write('Destination: ' + str(destination)+ '\n')
    itinerary_file.write('Length of stay: ' + str(length_of_stay)+ '\n')
    itinerary_file.write('Cost: $' + str(format(cost, ',.2f')) + '\n')

    # Close the file
    itinerary_file.close()


# Call main
main()
