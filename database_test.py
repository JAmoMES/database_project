import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = "INSERT INTO tag_new(tagID,tag_name) VALUES (?, ?)"
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


connection = sqlite3.connect('Steam_sql.db')
select = "SELECT tagname FROM tag"
cursor = connection.execute(select)

set_tag = set()

for row in cursor:
    row = str(row)
    row = row[2:len(row) - 3].split(';')
    for it in row:
        it = it.strip()
        set_tag.add(str(it))

set_tag = sorted(set_tag)

for i in enumerate(set_tag):
    create_task(connection, i)

connection.close()
