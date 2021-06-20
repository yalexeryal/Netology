class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avr_grade(self):
        if self.grades:
            sum_hw = 0
            count = 0
            for grades in self.grades.values():
                sum_hw += sum(grades)
                count += len(grades)
            return round(sum_hw / count, 2)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'\
              f'Средняя оценка за ДЗ: {self.get_avr_grade()} \n'\
              f'Законченные куры обучения: {self.finished_courses} \n'\
              f'Курсы в процессе обучения: {self.courses_in_progress} \n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет.')
            return
        else:
            compare = self.get_avr_grade() < other_student.get_avr_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}')
        return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname}'
        return res



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'\
              f'Средняя оценка за лекции: {sum(self.grades) / len(self.grades) :.2f} \n'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет.')
            return
        else:
            compare = round(sum(self.grades) / len(self.grades), 2) \
                      < round(sum(other_lecturer.grades) / len(other_lecturer.grades), 2)
            if compare:
                print(f'{self.name} {self.surname} оценивается студентами хуже, чем '
                      f'{other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{other_lecturer.name} {other_lecturer.surname} оценивается студентами хуже, чем '
                      f'{self.name} {self.surname}')
        return compare


first_student = Student('Иван', 'Иванов', 'м')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Git']

second_student = Student('Петр', 'Петров', 'м')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']

first_reviwer = Reviewer('Николай', 'Пупкин')
first_reviwer.courses_attached += ['Python']
first_reviwer.courses_attached += ['Git']

first_reviwer.rate_hw(first_student, 'Python', 9)
first_reviwer.rate_hw(first_student, 'Python', 7)
first_reviwer.rate_hw(first_student, 'Python', 5)

first_reviwer.rate_hw(first_student, 'Python', 7)
first_reviwer.rate_hw(second_student, 'Git', 6)
first_reviwer.rate_hw(second_student, 'Git', 10)
first_reviwer.rate_hw(second_student, 'Python', 8)

first_lecturer = Lecturer('Аристарх', 'Луначарский')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']
second_lecturer = Lecturer('Никола', 'Тесла')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Git', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer,  'Git', 10)

print(first_lecturer.grades)
print(second_lecturer.grades)

print(first_student.grades)
print(second_student.grades)

print(first_student < second_student)
print(first_lecturer < second_lecturer)

print('Student')
print(first_student)
print(second_student)

print('Reviewer')
print(first_reviwer)

print('Lecturer')
print(first_lecturer)
print(second_lecturer)

def get_avg_hw_grade(student_list, course):
    total_sum = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)


print(get_avg_hw_grade([first_student, second_student], 'Python'))


def get_avg_lect_grade(list_lect):
    total_sum = 0
    for lecturer in list_lect:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return total_sum / len(list_lect)


print(get_avg_lect_grade([first_lecturer, second_lecturer]))