class Dog:
    # Class variable (common to all dogs)
    species = "Canis familiaris"

    def __init__(self, breed, age):
        # Instance variables (different for each dog)
        self.breed = breed
        self.age = age

    def display_details(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age, "years")
        print("----------------------")


# Creating two objects of different breeds
dog1 = Dog("German Shepherd", 5)
dog2 = Dog("Labrador", 3)

# Display details
dog1.display_details()
dog2.display_details()