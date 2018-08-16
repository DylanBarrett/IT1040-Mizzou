import Animal


print('Welcome to the animal generator!')
print('This program creates Animal objects.')

animals = []

while(True):
    animal = input('\nWhat type of animal would you like to create? ')
    
    name = input("What is the animal's name? ", )
    
    new_animal = Animal.Animal(animal, name)
    animals.append(new_animal)
    
    again = input("\nWould you like to add more animals (y/n)? ")
    if(again != 'y'):
        break
            
print("\nAnimal List")
print("------------")

for n in animals:
    print(n.get_name(), 'the', n.get_animal_type(), 'is', n.check_mood())
    
