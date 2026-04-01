from animal import Animal
from dog import Dog
from Bird import bird

if __name__ == "__main__":
    #object of the animal class instance of the animal class. intanciation the class
    animal1 = Animal("Gus", "Mouse")

    dog2 = Dog("Draco", "Canine", "Large")

    animal2 = bird("Tweetie", "Bird", "Blue")

    print(animal1)
    animal1.speak()
    
    print(dog2)
    dog2.speak()
    dog2.preform_trick("dance")
    print(dog2.name)

    dog2.set_age(-1)
    dog2.set_age(3)

    print(animal2)
    animal2.speak()

    # TODO: Create an instance of the Animal class
    # TODO: Print the Animal instance
    # TODO: Call the method to make a generic animal sound

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals
