#blueprint
class Animal:
    """
    Base class representing a generic animal.
    """
    # class level perameter or attribute
    kingdom = "Animalia"

    #object specific attributtes 
    def __init__(self, name, species):
        self.name = name
        self.species = species 

    # class method
    def speak(self):
        print(f"{self.name} makes a noise\n")

    #magic methods changes how print(object) behaves override
    def __str__(self):
        return (f"Kingdom: {self.kingdom}\n"
                f"Name: {self.name}\n"
                f"Species: {self.species}\n")

