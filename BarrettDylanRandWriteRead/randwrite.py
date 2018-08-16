# This program writes random numbers
# in the range of 1 through 999 to a file
import random

print("The purpose of this program is to randomly generate numbers in the range of 1-999. \n")

# User selects the nonzero positive number to generate
while (True):
    try:
        quantity = int(input("How many numbers would you like to generate?: "))
        if (quantity <= 0):
            print("The value you entered is invalid. Only nonzero positive integers are valid.")
            continue
    except ValueError:
        print("The value you entered is invalid. Only nonzero positive integers are valid.")
    else: break

# Define the main function
def main():
    # Open a file named randnum.txt.
    outfile = open('randnum.txt', 'w')
    
    #Generate numbers to the file.
    for count in range(quantity):
        outfile.write(str(random.randint(1,999)) + '\n')

    # Close the file
    outfile.close()
    print("The numbers were written to randnum.txt.")
                                    
# Call the main function.
main()


