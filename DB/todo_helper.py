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
        print(str(row[0]) + " --> ", row[1])

# update the data
def update_task(idx , updated_task ):
    # update table_name set column_name=new_value where ID=index
    cur.execute("UPDATE " +  table_name + " SET taskname = (?) WHERE id = (?)", [updated_task,idx] )
    print("Task updated successfully")
    con.commit()


# delete the data
def delete_task(idx):
    # delete from table_name where id = index
    cur.execute("DELETE from " + table_name + " WHERE id = (?)" , [idx])
    print("Task deleted successfully!")
    con.commit()

def close_connection():
    cur.close()
    con.close()