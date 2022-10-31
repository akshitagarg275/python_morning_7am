import sqlite3

con = sqlite3.connect("todo.db")

cur = con.cursor()
table_name = 'todos'
# create a table
# create table if not exists table_name (id integer primary key autoincrement, taskname text)
def create_table():
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id integer primary key autoincrement, taskname text) '
    cur.execute(sql)

# Adding todo in the table
def add_todo(todo_name):
    # insert into table_name (column_name) values (column_values)
    cur.execute("INSERT INTO " + table_name + " (taskname) VALUES (?)", [todo_name])
    print("TODO added in the database successfully!!")
    con.commit()

# Read data from the table
def read_todos():
    # select column_name1, column_name2 from table_name
    # select * from table_name
    cur.execute("SELECT * from " + table_name)

    for row in cur.fetchall():
        print(row[0] + " --> ", row[1])

# update the data

# delete the data