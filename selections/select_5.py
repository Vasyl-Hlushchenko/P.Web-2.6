import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("./dbhw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.full_name, s.subject_name
FROM teachers as t
LEFT JOIN subjects as s ON s.teacher_id = t.id
WHERE t.id = 1
"""


print(execute_query(sql))
