from datetime import datetime
import faker
from random import randint, choice, shuffle
import sqlite3

NUMBER_STUDENTS = 39
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 6
NUMBER_TEACHERS = 4
NUMBER_MARKS = 16
MAX_MARK = 12


def generate_fake_data():
    fake_students = []
    fake_groups = []
    fake_subjects = []
    fake_teachers = []
    fake_dates = []
    fake_marks = []

    fake_data = faker.Faker()

    for _ in range(NUMBER_STUDENTS):
        fake_students.append(fake_data.name())

    for i in range(NUMBER_GROUPS):
        fake_groups.append(f"group- {i + 1}")

    for _ in range(NUMBER_SUBJECTS):
        fake_subjects.append(fake_data.job())

    for _ in range(NUMBER_TEACHERS):
        fake_teachers.append(fake_data.name())

    for _ in range(NUMBER_MARKS):
        fake_dates.append((fake_data.date_this_year()).strftime("%d.%m.%Y"))

    for _ in range(NUMBER_MARKS):
        fake_marks.append(randint(1, MAX_MARK))


    return fake_students, fake_groups, fake_subjects, fake_teachers, fake_dates, fake_marks


def prepare_data(students, groups, subjects, teachers, dates, marks):
    for_students = []
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_groups = []
    for group in groups:
        for_groups.append((group,))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))
    
    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    for_marks = []
    for student in students:
        for _ in range(NUMBER_MARKS):
            for_marks.append((student, randint(1, len(subjects)+1), choice(marks), choice(dates)))
    

    return for_students, for_groups, for_subjects, for_teachers, for_marks


def insert_data_to_db(students, groups, subjects, teachers, marks):

    with sqlite3.connect('dbhw.db') as con:

        cur = con.cursor()

        sql_to_students = """INSERT INTO students(full_name, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_teachers = """INSERT INTO teachers(full_name)
                              VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_marks = """INSERT INTO marks(student_id, subject_id, mark, date)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)

        con.commit()


if __name__ == "__main__":
    students, groups, subjects, teachers, marks = prepare_data(*generate_fake_data())
    insert_data_to_db(students, groups, subjects, teachers, marks)