import statistics

# Load the numbers from a file into an array.
def load_numbers(filename):

    numbers = []  # to hold the list of numbers

    try: 
        number_file = open(filename, "r")
        for number in number_file:
            number = int(number)  # Convert the read string to an int.
            numbers.append(number)
    except Exception as err:
        print ("An error occurred loading", filename)
        print ("The error returned was", err)
        return numbers

    if (len(numbers) < 1):
        print ("There were no numbers in", filename)
        return numbers

    else:
        return numbers

# Perform the statistics calculations using the values
# in the numbers array.
def calculate_stats(numbers):
    mean = statistics.mean(numbers)
    print("mean = ", mean)
    median = statistics.median(numbers)
    print("median = ", median)
    median_low = statistics.median_low(numbers)
    print("median_low = ", median_low)
    median_high = statistics.median_high(numbers)
    print("median_high = ", median_high)
    median_grouped = statistics.median_grouped(numbers)
    print("median_grouped = ", median_grouped)
    stdev = statistics.stdev(numbers)
    print("stdev = ", stdev)
    variance = statistics.variance(numbers)
    print("variance = ", variance)





  


# The main function that contains what the program is to do!
def main():
    do_evaluate = True
    while(do_evaluate):
        filename = input('\nWhat is the file you would like to evaluate? ')
        numbers = load_numbers(filename)
        if (len(numbers) > 0):
            calculate_stats(numbers)
        check_evaluate = input('\nWould you like to evaluate another file? (y/n) ')
        if (check_evaluate != 'y'):
            do_evaluate = False


# Call the main() function to make the program do what it is defined to do.
main()
