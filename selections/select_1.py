import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("./dbhw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.full_name, ROUND(AVG(m.mark),2) as avg
FROM students as s
LEFT JOIN marks as m ON s.id = m.student_id
GROUP BY full_name
ORDER BY avg DESC
LIMIT 5
"""


print(execute_query(sql))
