class Dog:
    species = "Canine"
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

blu = Dog("Golden Retriever", "Buddy" )
woo = Dog("German Shepherd", "Max"  )

print("Buddy is a {}".format(blu.species))
print("Max is also a {}".format(woo.species))
print("Dog 1 Details:")
print("Dog 2 Details:")

