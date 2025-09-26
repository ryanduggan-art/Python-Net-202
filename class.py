class Dog:
    tail = 'Wag'
    ears = 'Not Listening'

    def bark(self):
        print('Woof')

    def __init__(self, name):
        self.name = name


tuba = Dog('Tuba')
print(tuba.name)

tuba.tail = 'Missing'
tuba.bark()
