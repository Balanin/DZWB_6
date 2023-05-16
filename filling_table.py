from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
SUBJECTS = [
    "Vehicle Mechatronics ",
    "Active and Passive Car Safety Systems ",
    "Communication systems",
    "Artificial intelligence in electronics",
    "Digital Signal Processing",
    "Signal Processors",
    "ECAD design tools",
    "Sensor systems ",
]

def generate_fake_data( students, teachers) -> tuple():
    number_groups = []  # здесь будем хранить компании
    fake_students = []  # здесь будем хранить сотрудников
    fake_teachers = []  # здесь будем хранить должности
    '''Возьмём три компании из faker и поместим их в нужную переменную'''
    fake_data = faker.Faker()

    # Создадим набор компаний в количестве number_companies
    for _ in range(3):
        number_groups.append( randint(1, 3))

    # Сгенерируем теперь number_employees количество сотрудников'''
    for _ in range(students):
        fake_students.append(fake_data.name())

    # И number_post набор должностей
    for _ in range(teachers):
        fake_teachers.append(fake_data.name())

    return  fake_students, fake_teachers, number_groups


def prepare_data(student, teacher, number_groups) -> tuple():
    teachers = []

    for i in teacher:
        teachers.append((i,))



    groups = []
    for i in range(1, NUMBER_GROUPS + 1):
        groups.append((i,))


    subjects = []  
    for sub in SUBJECTS:
        subjects.append((sub, randint(1, 6)))


    students = []
    for i in student:
        students.append((i, randint(1,NUMBER_GROUPS)))

    marks = []
    for st in range( NUMBER_STUDENTS + 1):
        for mark_count in range(randint(1, 10)):
            mark_date = datetime(2022, randint(1, 12), randint(1, 28)).date()
            marks.append((st, randint(1, 8), randint(1, 5), mark_date))

    return (students, teachers, groups, subjects, marks)



def insert_data_to_db(students, teachers, groups, subjects, marks) -> None:
    # Создадим соединение с нашей БД и получим объект курсора для манипуляций с данными
    with sqlite3.connect('school.db') as con:
        cur = con.cursor()

        '''Заполняем таблицу компаний. И создаем скрипт для вставки, где переменные, которые будем вставлять отметим
        знаком заполнителя (?) '''

        sql_to_group = """INSERT INTO groups(groups_number)
                                VALUES (?)"""

        '''Для вставки сразу всех данных воспользуемся методом executemany курсора. Первым параметром будет текст
        скрипта, а вторым данные (список кортежей).'''

        cur.executemany(sql_to_group, groups)

        sql_to_teachers = """INSERT INTO teachers(name)
                               VALUES (?)"""

        # Данные были подготовлены заранее, потому просто передаем их в функцию

        cur.executemany(sql_to_teachers, teachers)

        # Далее вставляем данные о сотрудниках. Напишем для него скрипт и укажем переменные

        sql_to_students = """INSERT INTO students(student_name, group_id)
                              VALUES (?,?)"""

        cur.executemany(sql_to_students, students)


        # Последней заполняем таблицу с зарплатами

        sql_to_subject = """INSERT INTO subjects(subjects_name, teacher_id)
                              VALUES (?, ?)"""

        # Вставляем данные о зарплатах

        cur.executemany(sql_to_subject, subjects)

        sql_to_marks = """INSERT INTO marks(student_id, subject_id, mark, date_of)
                              VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_marks, marks)

        # Фиксируем наши изменения в БД

        con.commit()


if __name__ == "__main__":
    student, teacher, group, subject, mark = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS))
    insert_data_to_db(student, teacher, group, subject, mark)