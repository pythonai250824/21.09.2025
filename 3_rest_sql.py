
########################## CONTROLLER / ROUTER -- rest api (swagger, auth) and messages delegation
### communicates ONLY with BL

from fastapi import FastAPI, Query
import five_bl

app = FastAPI()

# JWT

@app.post("/messages/table")
def create_table():
    five_bl.create_table()
    return {'status': 'table messages created'}

@app.delete("/messages/table")
def drop_table():
    five_bl.drop_table()
    return {'status': 'table messages deleted'}

@app.post("/messages")
def insert_message(text):
    five_bl.insert_message(text)
    return {'status': f'message with text **{text}** created!'}

@app.put("/messages/{id}")
# missing: add if not exist ...
def update_message(id: int, text: str):
    operation = five_bl.update_or_create_message(id, text)
    return {'status': f'message {operation} with text {text}'}

@app.delete("/messages/{id}")
def delete_message(id: int):
    five_bl.delete_message(id)
    return {'status': f'message {id} deleted'}

@app.get("/messages")
def get_all_messages():
    try:
        result = five_bl.get_all_messages()
        return result
    except Exception as ex:
        print(ex)
        return { 'error': str(ex) }

@app.get("/messages/{id}")
def get_message_by_id(id: int):
    try:
        result = five_bl.delete_message(id)
        return result
    except:
        return {'status': f'message with id {id} not found!'}



