# simple class
class Room:
    n_student: int = 20

# class with __init__ function
# __init__ function is called whenever the class gets created
class School:
    def __init__(self, name: str, n_teacher: int):
        self.name = name
        self.n_teacher = n_teacher

# class with __str__ function
# __str__ function is called whenever object name gets called
class Teacher:
    def __init__(self, sub: str):
        self.subject = sub

    def __str__(self):
        return f'{self.subject}'

    # object method
    def get_sub(self):
        print(f'Subject name : {self.subject}')

if __name__ == '__main__':
    # ---------------------------
    r_one = Room()
    print(f'Number of students: {r_one.n_student}')

    # ---------------------------
    s_one = School('great school', 15)
    print(f'Name of the school one: {s_one.name}')

    s_two = School('w school', 10)
    print(f'Name of the school two: {s_two.name}')

    # ---------------------------
    t_one = Teacher('Science')
    print(f'Subject of t_one : {t_one}')

    # ---------------------------
    t_two = Teacher('Mathematics')
    # method
    t_two.get_sub()
    Teacher.get_sub(t_two)

