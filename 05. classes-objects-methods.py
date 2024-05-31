class Person:
    'Person base class'
    wants_to_hack = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('{} age is {}'.format(self.name, self.age))

    def birthday(self):
        print("Woohoo, it's someone's ({}) birthday! Let's celebrate".format(self.name))
        self.age += 1

bob = Person('bob', 30)
alice = Person('alice', 25)
lisa = Person('lisa', 50)

print(bob)
print(alice)
print(lisa)

print(bob.name)
print(bob.age)

bob.print_age()

bob.age = 31

bob.print_age()
bob.birthday()
bob.print_age()

print(hasattr(bob, "age"))
print(hasattr(bob, "xD"))

print(getattr(bob, "age"))

setattr(bob, "xD", 100)

print(getattr(bob, "xD"))

delattr(bob, "xD")

# print(getattr(bob, "xD"))


print(Person.wants_to_hack)
print(bob.wants_to_hack)
print(alice.wants_to_hack)
print(lisa.wants_to_hack)

Person.wants_to_hack = "No way!"

print(Person.wants_to_hack)
print(bob.wants_to_hack)
print(alice.wants_to_hack)
print(lisa.wants_to_hack)

bob.wants_to_hack = "Yes, let's hack!"

print(Person.wants_to_hack)
print(bob.wants_to_hack)
print(alice.wants_to_hack)
print(lisa.wants_to_hack)

print(bob.name)
# delattr(bob, name)
# del bob.name
# print(bob.name)

# del Person
# print(alice.name)
# bob2 = Person('bob2', 35)

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)

