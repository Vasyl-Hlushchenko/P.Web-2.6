import sqlite3


def execute_query(sql: str):
    with sqlite3.connect('./dbhw.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT c.full_name, s.subject_name, ROUND(AVG(m.mark),2) as avg
FROM students as c
LEFT JOIN marks as m ON c.id = m.student_id
LEFT JOIN subjects as s ON s.id = m.subject_id
WHERE m.subject_id = 1
GROUP BY full_name
ORDER BY avg DESC
LIMIT 1
"""


print(execute_query(sql))