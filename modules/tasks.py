from .database import connect
from prettytable import PrettyTable

def add_task(contact_id, description, due_date, status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (contact_id, description, due_date, status) VALUES (%s, %s, %s, %s)", (contact_id, description, due_date, status))
    conn.commit()
    cur.close()
    conn.close()

def list_tasks():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    table = PrettyTable(['id', 'contact id', 'description', 'due date', 'status'])
    for row in rows:
        table.add_row(row)
    print(table)
    cur.close()
    conn.close()

def update_task(task_id, contact_id, description, due_date, status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET contact_id=%s, description=%s, due_date=%s, status=%s WHERE id=%s", (contact_id, description, due_date, status, task_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_task(task_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
