import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("./dbhw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT m.mark
FROM marks as m
LEFT JOIN subjects as s ON s.id = m.subject_id
LEFT JOIN students as c ON c.id = m.student_id
LEFT JOIN groups as g ON c.group_id = g.id
WHERE g.id = 1 AND s.id = 1
"""


print(execute_query(sql))
