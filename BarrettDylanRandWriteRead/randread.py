# This program reads the numbers in randnum.txt
# and calculates the quantity of numbers

def main():

    try:
        # Open the randnum.txt file for reading.
        random = open('randnum.txt', 'r')
    
        # Initialize an accumulator to 0.0.
        Total = 0.0

        # Initialize a variable to keep count of the videos.
        count = 0

        print("List of random numbers in randnum.txt:")
    
        # Get the values from the file and count them.
        for line in random:
             # Convert a line to a string.
             number = str(line)
             number = number.rstrip('\n')

             # Add 1 to the count varibale.
             count += 1

             # Display the number.
             print(number)

        # Close the file.
        random.close()

        # Random number count
        print("\nRandom number count:", count)

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')

# Call the main function.
main()


