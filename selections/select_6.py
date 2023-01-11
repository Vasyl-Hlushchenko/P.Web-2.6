import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("./dbhw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.full_name
FROM students as s
LEFT JOIN groups as g ON s.group_id = g.id
WHERE g.group_name = 'group- 1'
"""


print(execute_query(sql))
