import sqlite3


def execute_query(sql: str):
    with sqlite3.connect('./dbhw.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT AVG(mark) FROM marks
"""


print(execute_query(sql))