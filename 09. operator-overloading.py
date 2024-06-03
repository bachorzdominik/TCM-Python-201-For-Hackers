print(1 + 1)
print("1" + "1")

class Person:
    'Person base class'
    wants_to_hack = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'My name is {} and I am {} years old'\
                    .format(self.name, self.age)

    def __add__(self, other):
        return self.age + other.age

    def __lt__(self, other):
        return self.age < other.age

    def print_name(self):
        print('My name is {}'.format(self.name))

    def print_age(self):
        print('{} age is {}'.format(self.name, self.age))

    def birthday(self):
        print("Woohoo, it's someone's ({}) birthday! Let's celebrate".format(self.name))
        self.age += 1

bob = Person('bob', 30)
alice = Person('alice', 25)

print(bob)
print(alice)
print(bob + alice)

print(bob < alice)
print(alice < bob)
