class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_avg = float()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        student_str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grade_avg}\n' \
                      f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                      f'Завершённые курсы: {", ".join(self.finished_courses)}\n '
        return student_str

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        else:
            return self.grade_avg > other.grade_avg

    def avg(self):
        avg_list = []
        grade_list = list(self.grades.values())
        if len(grade_list):
            for grade in grade_list:
                avg = sum(grade) / len(grade)
                avg_list.append(avg)
            avg = round(sum(avg_list) / len(avg_list), 1)
            return avg
        else:
            print('Оценок нет')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.grade_avg = float()

    def __str__(self):
        lecturer_str = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grade_avg}\n'
        return lecturer_str

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        else:
            return self.grade_avg > other.grade_avg

    def avg(self):
        avg_list = []
        grade_list = list(self.grades.values())
        if len(grade_list):
            for grade in grade_list:
                avg = sum(grade) / len(grade)
                avg_list.append(avg)
            avg = round(sum(avg_list) / len(avg_list), 1)
            return avg
        else:
            print('Оценок нет')
            return


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_str = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return reviewer_str


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress = ['Python', 'GIT']
best_student.finished_courses = ['Введение в программирование']

good_student = Student('Uory', 'Amen', 'your_gender')
good_student.courses_in_progress = ['Python', 'GIT']
good_student.finished_courses = ['Введение в программирование']

cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.courses_attached = ['Введение в программирование']

good_lecturer = Lecturer('Good', 'Lecturer')
good_lecturer.courses_attached = ['Введение в программирование']

cool_reviewer = Reviewer('Cool', 'Reviewer')
strict_reviewer = Reviewer('Strict', 'Reviewer')
cool_reviewer.courses_attached = ['Python', 'GIT']
strict_reviewer.courses_attached = ['Python', 'GIT']


cool_reviewer.rate_hw(best_student, 'Python', 10)
strict_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'GIT', 10)
strict_reviewer.rate_hw(best_student, 'GIT', 9)
cool_reviewer.rate_hw(best_student, 'GIT', 10)

cool_reviewer.rate_hw(good_student, 'Python', 9)
strict_reviewer.rate_hw(good_student, 'Python', 8)
cool_reviewer.rate_hw(good_student, 'Python', 10)
cool_reviewer.rate_hw(good_student, 'GIT', 8)
strict_reviewer.rate_hw(good_student, 'GIT', 7)
cool_reviewer.rate_hw(good_student, 'GIT', 8)

best_student.rate_hw(cool_lecturer, 'Введение в программирование', 10)
best_student.rate_hw(cool_lecturer, 'Введение в программирование', 10)
good_student.rate_hw(cool_lecturer, 'Введение в программирование', 9)
good_student.rate_hw(cool_lecturer, 'Введение в программирование', 10)

best_student.rate_hw(good_lecturer, 'Введение в программирование', 8)
best_student.rate_hw(good_lecturer, 'Введение в программирование', 9)
good_student.rate_hw(good_lecturer, 'Введение в программирование', 8)
good_student.rate_hw(good_lecturer, 'Введение в программирование', 10)

best_student.grade_avg = best_student.avg()
cool_lecturer.grade_avg = cool_lecturer.avg()

good_student.grade_avg = good_student.avg()
good_lecturer.grade_avg = good_lecturer.avg()

print(best_student)
print(good_student)
print(cool_lecturer)
print(good_lecturer)
print(cool_reviewer)
print(strict_reviewer)

if best_student.__gt__(good_student):
    print(f'{best_student.name} {best_student.surname} лучший студент!')
else:
    print(f'{good_student.name} {good_student.surname} лучший студент!')

if cool_lecturer.__gt__(good_lecturer):
    print(f'{cool_lecturer.name} {cool_lecturer.surname} лучший лектор!')
else:
    print(f'{good_lecturer.name} {good_lecturer.surname} лучший лектор!')

students_list = [best_student, good_student]
lecturers_list = [cool_lecturer, good_lecturer]


def students_grade_avg(students, course):
    grades_list = []
    avg_list = []
    for student in students:
        grades_list.append(student.grades[course])
    if len(grades_list):
        for grade in grades_list:
            avg = sum(grade) / len(grade)
            avg_list.append(avg)
        avg = round(sum(avg_list) / len(avg_list), 1)
        print(f'Средняя оценка за курс {course} у студентов - {avg}')
    else:
        return 'Ошибка'


def lecturers_grade_avg(lecturers, course):
    grades_list = []
    avg_list = []
    for lecturer in lecturers:
        grades_list.append(lecturer.grades[course])
    if len(grades_list):
        for grade in grades_list:
            avg = sum(grade) / len(grade)
            avg_list.append(avg)
        avg = round(sum(avg_list) / len(avg_list), 1)
        print(f'Средняя оценка за курс {course} у лекторов - {avg}')
    else:
        return 'Ошибка'


students_grade_avg(students_list, 'Python')
lecturers_grade_avg(lecturers_list, 'Введение в программирование')
