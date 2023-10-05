class Animal:

    def make_sound(slef):
        pass

class Dog(Animal):
    
    def make_sound(slef):
        print("woff")

class cat(Animal):
    def make_sound(slef):
        print("Meow")


def anmial_sound(animal):
    return animal.make_sound()
                   

dog=Dog()
Cat=cat()

print(anmial_sound(dog))
print(anmial_sound(Cat))