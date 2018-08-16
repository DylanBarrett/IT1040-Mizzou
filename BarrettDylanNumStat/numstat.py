# Program contains the ability to read a integer numbers from a file's contents
# and generate the sum, count, average, maximum, minimum, and range.



def main():
    num_stat = True
    while (num_stat):
        # Ask the user for the name of the file
        file_name = (input("What is the name of the file?: "))

        try:
            infile = open(file_name, 'r')

            # Read the contents of the file into a list.

            # Start a count
            count = 0
            # Start an accumulator
            total = 0.0

            largestInt = 0

            smallestInt = float('inf')

            for line in infile:
                # Convert a line to a string.
                number = int(line)

                # Add 1 to the count varibale.
                count += 1

                # Calculate the sum.
                total += number

                # Calculate the average.
                average = total / count

                # Find the maximum.
                if largestInt < number:
                    largestInt = number

                # Find the minimum.
                if smallestInt > number:
                    smallestInt = number

                # Find the range.
                num_range = largestInt - smallestInt

            infile.close()

            # Display the information.    
            print("File name: ", file_name)
            print("Sum: ", total)
            print("Count: ", count)
            print("Average: ", average)
            print("Maximum: ", largestInt)
            print("Minimum: ", smallestInt)
            print("Range: ", num_range)

        except:
            print('An error occured trying to open or read the file.')

        more_stats = input('Would you like to evaluate another file? (y/n): ')
        if (more_stats !="y"):
            num_stat = False



main()
