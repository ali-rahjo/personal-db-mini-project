from modules.database import connect
from prettytable import PrettyTable

def due_tasks_report():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE due_date < CURRENT_DATE AND status != 'completed'")
    rows = cur.fetchall()
    table = PrettyTable(['id', 'contact id', 'description', 'due date', 'status'])
    for row in rows:
        table.add_row(row)
    print(table)
    cur.close()
    conn.close()

def contact_tasks_report(contact_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE contact_id = %s", (contact_id,))
    rows = cur.fetchall()
    table = PrettyTable(['id', 'contact id', 'description', 'due date', 'status'])
    for row in rows:
        table.add_row(row)
    print(table)
    cur.close()
    conn.close()
