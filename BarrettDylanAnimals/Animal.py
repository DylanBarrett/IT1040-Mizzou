import random

# This program creates a class named 
# Animal and stores information about an animal.

class Animal:
    
    # The __init__ method initializes the attribute
    
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        a = random.randint(1,3)
        if a ==1:
            self.__mood = 'happy'
        if a ==2:
            self.__mood = 'hungry'
        if a ==3:
            self.__mood = 'sleepy'
    
    # get_animal_type returns the type of animal
    def get_animal_type(self):
        return self.__animal_type
    
    # get_name returns the name of the animal
    def get_name(self):
        return self.__name
    
    # check_mood return the mood of the animal
    def check_mood(self):
        return self.__mood
    
    
