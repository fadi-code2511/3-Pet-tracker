# Part 1:
# Create a Pet class
# Attributes: name, species, age, adopted (boolean, default False)
# Constructor that initializes all of these.
# Method: display_info() → prints all pet data in a readable sentence.
# Method: mark_adopted() → sets adopted to True.
# Method: birthday() → increases the pet's age by 1 year.
# Create at least 3 pet objects, and call their methods and print the results to verify your work.

# Create a Pet class
class Pet:
    def __init__(self,name,species,age,adopted=False):  # constructor
        self.name=name
        self.species=species
        self.age=age
        self.adopted=adopted
