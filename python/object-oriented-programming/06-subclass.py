class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def school_name(self):
        print(f'{self.name}')

class Teacher(School):
    def __init__(self, name, location, subject):
        School.__init__(self, name, location)
        self.subject = subject

class Student(School):
    def __init__(self, name, location, roll_no):
        super().__init__(name, location)
        self.roll_no = roll_no

def main():
    t_1 = Teacher('Manav Rachna', 'Faridabad', 'Science')
    t_1.school_name()
    print(t_1.subject)
    s_1 = Student('Manav Rachna', 'Faridabad', 1)
    s_1.school_name()
    print(s_1.roll_no)

if __name__ == '__main__':
    main()

