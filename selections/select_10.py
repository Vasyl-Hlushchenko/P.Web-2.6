import sqlite3


def execute_query(sql: str):
    with sqlite3.connect('./dbhw.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT c.subject_name
FROM students as s
LEFT JOIN marks as m ON m.student_id = s.id
LEFT JOIN subjects as c ON m.subject_id = c.id
LEFT JOIN teachers as t ON c.teacher_id = t.id
WHERE s.id = 9 AND t.id = 1
GROUP BY c.subject_name
"""


print(execute_query(sql))