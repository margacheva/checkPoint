class Person():
    def __init__(self, surname, dayOfBirth, yearOfBearth):
        self.surname = surname
        self.dayOfBirth = dayOfBirth
        self.yearOfBearth = yearOfBearth

    def print_info(self):
        print('Фамилия:', self.surname)
        print('Дата рождения:',self.dayOfBirth, self.yearOfBearth)

    def age(self):
        print('Фамилия:', self.surname)
        print('Возраст:',2022 - self.yearOfBearth)

class Enrollee(Person):
    def __init__(self, surname, dayOfBirth, yearOfBearth, faculty):
        super().__init__(surname, dayOfBirth, yearOfBearth)
        self.faculty = faculty

    def info(self):
        print('Фамилия', self.surname)
        print('Дата рождения:', self.dayOfBirth, self.yearOfBearth)
        print('Факультет:', self.faculty)


class Student(Person):
    def __init__(self, surname, dayOfBirth, yearOfBearth, faculty,course):
        super().__init__(surname, dayOfBirth, yearOfBearth)
        self.faculty = faculty
        self.course = course

    def info(self):
        print('Фамилия', self.surname)
        print('Дата рождения:',self.dayOfBirth, self.yearOfBearth)
        print('Факультет:', self.faculty)
        print('Курс:', self.course)


class Teacher(Person):
    def __init__(self, surname, dayOfBirth, yearOfBearth, faculty, post, experience):
        super().__init__(surname, dayOfBirth, yearOfBearth)
        self.faculty = faculty
        self.post = post
        self.experience = experience

    def info(self):
        print('Фамилия', self.surname)
        print('Дата рождения:',self.dayOfBirth, self.yearOfBearth)
        print('Факультет:', self.faculty)
        print('Должность:', self.post)
        print('Стаж:', self.experience)
person1 = Person('Воронин','16.02.', 2004)
person2 = Person('Ягодкина','09.11.', 1999)
enrolle1 = Enrollee('Иванова','23.07.', 2001, 'История')
enrolle2 = Enrollee('Федоров','12.02.', 2005, 'Информатика')
student1 = Student('Кощеев','29.12.', 2000, 'Математика', '1')
student2 = Student('Голышева','01.12.', 1999, 'Инженерия', '3')
teacher1 = Teacher('Коровин','02.13.', 1980, 'История', 'Преподователь', '15 лет')
teacher2 = Teacher('Семенова','05.05.', 1978, 'Режиссура', 'Ректор', '25 лет')
listall = [person1, person2,enrolle1, enrolle2,student1, student2, teacher1, teacher2]
for i in listall:
    




