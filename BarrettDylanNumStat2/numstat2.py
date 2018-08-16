# Program contains the ability to read an integer numbers from a file's contents
# and generate the sum, count, average, maximum, minimum, range, median and mode.
import statistics

# Loop the program
while (True):
    
    # Start variables
    number_sum = 0
    number_count = 0
    number_average = 0
    number_maximum = 0
    number_minimum = 0
    number_range = 0
    mode = 0
    mode_freq = 0

    try:
        # Ask the user for a file of random numbers
        file_name = input("Enter the name of the file you would like to process: ")

        # Open the file
        number_file = open(file_name, "r")

        # Read the file's contents as a list of strings
        unconverted_numbers = number_file.readlines()

        # Create an empty list to store the converted numbers
        converted_numbers = []
        
        # Creat an empty dictionary
        number_counts = {}

        # Convert the strings to integers and store them in converted_numbers list
        for number in unconverted_numbers:
            converted_numbers.append(int(number))
            
        # Creat an empty dictionary
        number_counts = {}
        
        # Determine the sum
        number_sum = sum(converted_numbers)
        # Determine the count
        number_count = len(converted_numbers)
        # Determine the max
        number_maximum = max(converted_numbers)
        # Determine the minimum
        number_minimum = min(converted_numbers)
        # Calculate the average
        number_average = number_sum / number_count
        # Calculate the range
        number_range = number_maximum - number_minimum
        # Find the median
        median = statistics.median(converted_numbers)
        # Find the Mode
        mode = []
        for number in converted_numbers:
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1
        for number, freq in number_counts.items():
            if freq > mode_freq:
                mode_freq = freq
        for number, freq in number_counts.items():
            if mode_freq == freq:
                mode.append(number) 

        # Close the file
        number_file.close()

    # If there's a problem reading the file, print an error
    except Exception as err:
        print ('An error occurred reading', file_name)
        print ('The error is', err)

    # If the file was read successfully...
    else:
        # Print the calculated statistics
        print("File name:", file_name)
        print("Sum:", number_sum)
        print("Count:", number_count)
        print("Average:", number_average)
        print("Maximum:", number_maximum)
        print("Minimum:", number_minimum)
        print("Range:", number_range)
        print("Median:", median)
        print("Mode:", str(mode)[1:-1])

        # Ask to try again
        calculate_again = input("Would you like to evaluate another file? (y/n) ")
        if (calculate_again != "y"):
            break
