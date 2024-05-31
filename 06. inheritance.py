class Person:
    'Person base class'
    wants_to_hack = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print('My name is {}'.format(self.name))

    def print_age(self):
        print('{} age is {}'.format(self.name, self.age))

    def birthday(self):
        print("Woohoo, it's someone's ({}) birthday! Let's celebrate".format(self.name))
        self.age += 1


class Hacker(Person):
    def __init__(self, name, age, cves):
        super().__init__(name, age)
        self.cves = cves

    def print_name(self):
        print('My name is {} and I have {} CVEs'.format(self.name, self.cves))

    def total_cves(self):
        return self.cves


bob = Person('bob', 30)
alice = Hacker('alice', 25, 5)

bob.print_name()
alice.print_name()

print(bob.age)
print(alice.age)

bob.birthday()
alice.birthday()

print(bob.age)
print(alice.age)

print(alice.total_cves())
# print(bob.total_cves())

print(issubclass(Hacker, Person))
print(issubclass(Person, Hacker))

print(isinstance(bob, Person))
print(isinstance(bob, Hacker))

