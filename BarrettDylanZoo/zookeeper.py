import Animal
import zoo

def main():
    # Create a Zoo object
    z = zoo.Zoo()
    
    # This program will loop until the user says to exit
    while True:
        
        # Print zoo options
        print("Zoo Options")
        print("-----------")
        print("1. Add Animal")
        print("2. Show Animals")
        print("3. Exit")
        print()

        # Ask for a choice
        while True:
            try:
                choice = int(input("What would you like to do? "))
                if choice < 1 or choice > 3:
                    print("Please select a valid option.\n")
                    continue
            except ValueError:
                print("Please enter a numeric value.\n")
            else:
                break

        # Add Animal
        if choice == 1:
            # Ask the user for the animal's type and name
            animal_type = input("\nWhat type of animal would you like to create? ")
            animal_name = input("What is the animal's name? ")
            print()

            # Create a new Animal object
            animal = Animal.Animal(animal_type, animal_name)

            # Add the Animal to the Zoo
            z.add_animal(animal)

        if choice == 2:
            z.show_animals()

        if choice == 3:
            print("\nThank you for visiting the zoo!")
            break

       
main()

        
        
        
