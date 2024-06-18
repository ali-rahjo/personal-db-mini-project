import psycopg2
from psycopg2 import sql

def connect():
    return psycopg2.connect(dbname="my_personal_db", user="postgres", password='postgres', port="5438")

def create_tables():
    commands = (
        """
        CREATE TABLE contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(15),
            email VARCHAR(100)
        );
        """,
        """
        CREATE TABLE tasks (
            id SERIAL PRIMARY KEY,
            contact_id INTEGER REFERENCES contacts(id),
            description TEXT,
            due_date DATE,
            status VARCHAR(20)
        );
        """
    )
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
