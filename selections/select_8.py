import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("./dbhw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(m.mark),2) as avg
FROM marks as m
LEFT JOIN subjects as s ON m.subject_id = s.id
LEFT JOIN teachers as t ON t.id = s.teacher_id
WHERE t.id = 1 AND s.id = 1
"""


print(execute_query(sql))
