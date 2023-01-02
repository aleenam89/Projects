import sys

name = sys.argv[1]


class person:
    def __init__(self, name):
        self.name = name
        pass
    def hello(self):
        print(f'My name is {name} and I am a {type(self).__name__}')

def main():
    person_1 = person(name)
    person_1.hello()


main()

x = person(1)
print (x.__class__)
