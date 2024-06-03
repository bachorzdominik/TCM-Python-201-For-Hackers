print(len("string"))
print(len(['l','i','s','t']))

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
alice = Hacker('alice', 25, 10)

people = [bob, alice]

for person in people:
    person.print_name()
    print(type(person))
print('-'*40)

def obj_dump(object):
    object.print_name()
    print(object.age)
    object.birthday()
    print(object.age)
    print(object.__class__)
    print(object.__class__.__name__)

obj_dump(bob)
print('-'*40)
obj_dump(alice)
