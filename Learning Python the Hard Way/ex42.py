## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Person is-a object that has a pet
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## person has some kind of pet
        self.pet = None

## Employee is a person with a salary
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a dog:
rover = Dog("Rover")

## Satan is-a cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

## Mary has a pet named Satan
mary.pet = satan

## Frank is an employee who makes 120000
frank = Employee("Frank", 120000)

## Frank has a pet name Rover
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()




