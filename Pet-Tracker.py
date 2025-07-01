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
    
    # prints all pet data in a readable sentence.
    def display_info(self):
        if self.adopted==True:
            print(f"{self.name} is a {self.species}, and it has {self.age} years old and it has been adopted")
        else:
            print(f"{self.name} is a {self.species}, and it has {self.age} years old and it hasn't been adopted yet")
    
    # sets adopted to True
    def mark_adopted(self):
        self.adopted=True



# for testing purpose
pet1 = Pet("sally", "cat", 3)
pet1.display_info()
pet1.mark_adopted()
pet1.display_info()

# pet2 = Pet("Max", "dog", 5, adopted=True)
# pet2.display_info()

