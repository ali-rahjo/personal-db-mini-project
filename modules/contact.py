from modules.database import connect
from prettytable import PrettyTable

def add_contact(name, phone, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    conn.commit()
    cur.close()
    conn.close()

def list_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    table = PrettyTable(['id', 'name', 'phone', 'email'])
    for row in rows:
        table.add_row(row)
    print(table)
    cur.close()
    conn.close()

def update_contact(contact_id, name, phone, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET name=%s, phone=%s, email=%s WHERE id=%s", (name, phone, email, contact_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_contact(contact_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
    conn.commit()
    cur.close()
    conn.close()
