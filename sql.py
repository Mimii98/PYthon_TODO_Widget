import sqlite3


connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        done INTEGER DEFAULT 0
    )
""")

def add_todo(text):
    connection = sqlite3.connect("todos.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO todos (text, done) VALUES (?, ?)",
        (text, 0)
    )


def get_todos():
    connection = sqlite3.connect("todos.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos")
    rows = cursor.fetchall()
    connection.close()
    return rows

def toggle_done(todo_id, done):
    connection = sqlite3.connect("todos.db")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE todos SET done = ? WHERE id = ?",
        (done, todo_id)
    )
def delete_todo(todo_id):
    connection = sqlite3.connect("todos.db")
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM todos WHERE id = ?",
        (todo_id,)
    )
    


print(get_todos())
connection.commit()
connection.close()

