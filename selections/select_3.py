import sqlite3


def execute_query(sql: str):
    with sqlite3.connect("./dbhw.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.subject_name, g.group_name, ROUND(AVG(m.mark),2) as avg
FROM marks as m, groups as g
LEFT JOIN subjects as s ON s.id = m.subject_id
LEFT JOIN students as c ON c.group_id = g.id
WHERE m.subject_id = 1 AND g.group_name = "group- 1"
"""


print(execute_query(sql))
