
import sqlite3

def get_cursor():
    conn = sqlite3.connect("messages_db.db")
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    conn, cursor = get_cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL)
    """)
    conn.commit()
    conn.close()

def drop_table():
    conn, cursor = get_cursor()
    cursor.execute("""
    DROP TABLE messages
    """)
    conn.commit()
    conn.close()

def insert_message(text):
    conn, cursor = get_cursor()
    cursor.execute("""
    INSERT INTO messages (text) VALUES (?);
    """, (text,))
    conn.commit()
    conn.close()

def update_message(id: int, text: str):
    conn, cursor = get_cursor()
    cursor.execute("""
    UPDATE messages SET text = ? WHERE id = ?;
    """, (text, id))
    conn.commit()
    conn.close()

def delete_message(id: int):
    conn, cursor = get_cursor()
    cursor.execute("""
    DELETE messages WHERE id = ?;
    """, (id))
    conn.commit()
    conn.close()

def get_all_messages():
    conn, cursor = get_cursor()
    cursor.execute("""
    SELECT * from messages;
    """)
    return cursor.fetchall()

def get_message_by_id(id: int):
    conn, cursor = get_cursor()
    cursor.execute("""
    SELECT * from messages WHERE id = ?;
    """, (id, ))
    return cursor.fetchall()


