from animal import Animal

#child class of Animal
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    # kingdom
    # name species
    # Speak()
    #__str__
    def __init__(self, name, species, size):
        super().__init__(name, species)
        self.size = size

    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n"
    
    def speak(self):
        print(f"{self.name} barks!\n")
    

    # TODO: Add a method for the dog to make a specific sound. 
    # Call the method `speak` and make it output a specific message like 
    # "The dog barks.