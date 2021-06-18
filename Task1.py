# Make a class structure in python representing people at school. Make a base class called Person,
# a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.
"""Сделал несколько функций, котрые больше подходят для университета, чем для школы,
 но таким образом увеличил количетсво методов и атрибутов"""


class Person:
    def __init__(self, name, surname, grade):
        self.name = name.title()
        self.valid_str(name, 'name')
        self.surname = surname.title()
        self.valid_str(surname, 'surname')
        self.grade = grade

    @staticmethod
    def valid_str(temp, description):
        """Функция используется для проверки переменных name и surname"""
        if not temp.isalpha():
            raise ValueError(f'Переменная \'{description}\' указана неправильно! '
                             f'Используйте только буквенные значения!')

    def greeting(self):
        """Приветствие"""
        print(f'Привет! Меня зовут {self.name} {self.surname}.')


class Student(Person):
    def __init__(self, name, surname, grade, avg_mark, failure, social_scholarship):
        Person.__init__(self, name, surname, grade)
        self.valid_grade()
        self.avg_mark = avg_mark
        self.failure = failure  # количество проваленных экзаменов
        self.social_scholarship = social_scholarship.lower()  # претендует ли студент на социальную стипендию
        self.type_of_scholarship = 'none'
        self.scholarship = 0
        self.set_scholarship()

    def valid_grade(self):
        """Функция проверяет тип данных переменной grade"""
        if not isinstance(self.grade, int):
            raise ValueError(f'Переменная \'grade\' указана неправильно! Используйте только целочисленные значения')

    def get_type_of_scholarship(self):
        """Функция определяет тип стипендии в зависимости от успеваемости"""
        if self.failure >= 1:
            self.type_of_scholarship = 'none'
        elif self.avg_mark == 100:
            self.type_of_scholarship = 'president'
        elif self.avg_mark >= 90:
            self.type_of_scholarship = 'increased'
        elif self.avg_mark >= 75:
            self.type_of_scholarship = 'academic'
        elif self.social_scholarship == 'yes':
            self.type_of_scholarship = 'social'
        else:
            self.type_of_scholarship = 'none'

    def set_scholarship(self):
        """Функция назначает сумму стипендии в зависимости от её типа"""
        self.get_type_of_scholarship()
        if self.type_of_scholarship == 'social':
            self.scholarship = 1180
        elif self.type_of_scholarship == 'academic':
            self.scholarship = 1300
        elif self.type_of_scholarship == 'increased':
            self.scholarship = 1892
        elif self.type_of_scholarship == 'president':
            self.scholarship = 2130
        else:
            self.scholarship = 0

    def talk(self):
        self.greeting()
        print(f'Я учусь в {self.grade} классе. Моя средняя оценка: {self.avg_mark}, поэтому я', end=' ')
        if self.scholarship == 0:
            print('не получаю стипендию :(')
        else:
            print(f'получаю {self.type_of_scholarship} стипендию в размере {self.scholarship}.')


class Teacher(Person):
    def __init__(self, name, surname, grade, salary):
        Person.__init__(self, name, surname, grade)
        self.salary = salary

    def valid_grade(self):
        if not isinstance(self.grade, list):
            raise ValueError(f'Переменная \'grade\' указана неправильно! Используйте тип данных list')
        if not all(isinstance(x, int) for x in self.grade):
            raise ValueError(f'Переменная \'grade\' указана неправильно! '
                             f'Используйте только целочисленные значения внутри списка')

    def talk(self):
        self.greeting()
        print(f'Я преподаю в {self.grade} классах! По секрету скажу: моя зарплата составляет {self.salary}')


def main():
    student1 = Student('Misha', 'Barkov', 11, 80, 0, 'no')
    student1.talk()
    teacher1 = Teacher('Maksim', 'Shevchenko', [1, 2, 3, 4], 6000)
    teacher1.talk()


if __name__ == '__main__':
    try:
        main()
    except ValueError as massage:
        print(massage)
