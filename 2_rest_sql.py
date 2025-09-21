from fastapi import FastAPI, Query
import sqlite3

app = FastAPI()

def get_cursor():
    conn = sqlite3.connect("messages_db.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return conn, cursor

@app.post("/messages/table")
def create_table():
    conn, cursor = get_cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL)
    """)
    conn.commit()
    conn.close()
    return { 'status': 'table messages created'}

@app.delete("/messages/table")
def drop_table():
    conn, cursor = get_cursor()
    cursor.execute("""
    DROP TABLE messages
    """)
    conn.commit()
    conn.close()
    return {'status': 'table messages deleted'}

@app.post("/messages")
def insert_message(text):
    conn, cursor = get_cursor()
    cursor.execute("""
    INSERT INTO messages (text) VALUES (?);
    """, (text,))
    conn.commit()
    conn.close()
    return {'status': f'message with text **{text}** created!'}

@app.put("/messages/{id}")
# missing: add if not exist ...
def update_message(id: int, text: str):
    conn, cursor = get_cursor()
    cursor.execute("""
    UPDATE messages SET text = ? WHERE id = ?;
    """, (text, id))
    conn.commit()
    conn.close()
    return {'status': f'message id {id} updated with text {text}'}

@app.delete("/messages/{id}")
def delete_message(id: int):
    conn, cursor = get_cursor()
    cursor.execute("""
    DELETE FROM messages WHERE id = ?;
    """, (id,))
    conn.commit()
    conn.close()
    return {'status': f'message {id} deleted'}

@app.get("/messages")
def get_all_messages():
    try:
        conn, cursor = get_cursor()
        cursor.execute("""
        SELECT * from messages;
        """)

        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(dict(row))
        return result

    except Exception as ex:
        print(ex)
        return { 'error': str(ex) }

@app.get("/messages/{id}")
def get_message_by_id(id: int):
    conn, cursor = get_cursor()
    cursor.execute("""
    SELECT * from messages WHERE id = ?;
    """, (id, ))
    result = cursor.fetchone()
    if result:
        return dict(result)
    return {'status': f'message with id {id} not found!'}



