class Person:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.name} from {self.location}'

    def __repr__(self):
        return f'Person({self.name}, {self.location})'

    def __add__(self, other):
        return f'{self.name}{other.name}'

    def __len__(self):
        return len(self.name)

def main():
    nipuran = Person('Nipuran', 'Bharat')
    naruto = Person('Naruto', 'Konoha')
    #print(nipuran)
    #print(str(nipuran))
    #print(repr(nipuran))
    #print(nipuran.__str__())
    #print(nipuran.__repr__())
    print(len(nipuran))
    print(Person.__len__(naruto))
    print(naruto.__len__())
    print(nipuran+naruto)

if __name__ == '__main__':
    main()
