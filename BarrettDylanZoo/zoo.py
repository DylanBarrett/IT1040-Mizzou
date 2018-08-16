#define class
class Zoo:

    #The __init__ method initializes the attributes.
    def __init__(self):
        self.animal = []

    #The add_animals method adds animals to the list
    def add_animal(self, animal):
        self.animal.append(animal)

    #print the list of animals
    def show_animals(self):
        if len(self.animal) == 0:
            print('\nAnimal list')
            print('-------------')
            print('There are no animals in your zoo!',"\n")
        else:
            print('\nAnimal list')
            print('-------------')
            for n in self.animal:
                print(n.get_name(),'the', n.get_animal(), 'is', n.get_mood())
            print()
            
                
            
        
    

    
