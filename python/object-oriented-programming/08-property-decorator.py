class Person:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        #self.introduction = f'Hello, My name is {self.name}, I am from {self.location}'

    @property
    def introduction(self):
        return f'Hello, My name is {self.name}, I am from {self.location}'

    @introduction.setter
    def introduction(self, intro):
        self.name, self.location = intro.split()

    @introduction.deleter
    def introduction(self):
        print('Object deleted!!')
        self.name = None
        self.location = None

def main():
    person_1 = Person('Nipuran', 'India')
    person_2 = Person('Guido van Rossum', 'Netherlands')

#    print(person_1.introduction)
#    person_1.name = 'Dennis Ritchie'
#    print(person_1.name)
#    print(person_1.introduction)
    
    person_1.introduction = 'June America'
    print(person_1.introduction)
    del person_1.introduction
    

if __name__ == '__main__':
    main()
