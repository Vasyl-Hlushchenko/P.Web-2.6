from sqlite3 import Error
from connect import create_connection, database


sql_create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    id integer PRIMARY KEY AUTOINCREMENT,
    full_name text NOT NULL,
    group_id integer,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);
"""

sql_create_groups_table = """
CREATE TABLE IF NOT EXISTS groups (
    id integer PRIMARY KEY AUTOINCREMENT,
    group_name text NOT NULL
);
"""

sql_create_teachers_table = """
CREATE TABLE IF NOT EXISTS teachers (
    id integer PRIMARY KEY AUTOINCREMENT,
    full_name text NOT NULL
);
"""

sql_create_subjects_table = """
CREATE TABLE IF NOT EXISTS subjects (
    id integer PRIMARY KEY AUTOINCREMENT,
    subject_name text NOT NULL,
    teacher_id integer,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);
"""

sql_create_marks_table = """
CREATE TABLE IF NOT EXISTS marks (
    id integer PRIMARY KEY AUTOINCREMENT,
    student_id integer,
    subject_id integer,
    mark integer NOT NULL,
    date text NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
);
"""

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_groups_table)
            create_table(conn, sql_create_teachers_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_marks_table)
        else:
            print("Error! cannot create the database connection.")

