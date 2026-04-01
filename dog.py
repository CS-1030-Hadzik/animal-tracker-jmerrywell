from animal import Animal

# inheritance
# child class of Animal
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
        self.__age = 0 # encapsulation __ private data member in python. private

    # public method get the age of the dog
    # getter
    def get_age(self):
        return self.__age
        
    # setter
    def set_age(self, new_age):
        if new_age < 0:
            return print("The age needs to be positive.")
        self.__age = new_age
        self.print_dog_age()

    def print_dog_age(self):
        print(f"{self.name}'s age is now {self.__age}\n")

    def __str__(self): #polymorphism example
        return super().__str__() + f"Size: {self.size}\n"
    
    def speak(self): # polymorphism example
        print(f"{self.name} barks!\n")
    

    # dog to preform a trick
    # sit, lay down, stay, fetch, hand stand, shake
    # method that allowes us to have the dog object do a trick
    # perform_trick trick 
    def preform_trick(self, trick):
        # if trick=sit
        # then dog sit
        print(f"{self.name} ") 
        match trick:
            case "sit":
                print("sits down. ", end="")
            case "lay down":
                print("lays on the ground.\n")
            case "stay":
                print("stays still.\n")
            case "fetch":
                print("gets the stick.\n")
            case "hand stand":
                print("stands on frount two paws.\n")
            case "shake":
                print("shakes your hand\n")
            case _:
                print("looks confused\n")


            # if trick = lay down
            # then dog lay down

            # *....