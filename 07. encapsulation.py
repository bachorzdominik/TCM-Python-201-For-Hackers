class Person:
    'Person base class'
    wants_to_hack = True

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_name(self):
        print('My name is {}'.format(self.name))

    def print_age(self):
        print('{} age is {}'.format(self.name, self.age))

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def birthday(self):
        print("Woohoo, it's someone's ({}) birthday! Let's celebrate".format(self.name))
        self.__age += 1


bob = Person('bob', 30)
# print(bob.age)
print(bob.get_age())
bob.set_age(31)
print(bob.get_age())
bob.birthday()
print(bob.get_age())

print(bob.__dict__)
bob._Person__age = 50
print(bob.get_age())
