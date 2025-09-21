
###################### Business logic - program logic , not specific dal, general manager
### communicates ONLY with other BLs, and DAL


import four_dal as dal
# import pg_sql as dal

def create_table():
    dal.create_table()

def drop_table():
    dal.drop_table()

def insert_message(text):
    dal.insert_message(text)

def update_or_create_message(id: int, text: str):
    message = dal.get_message_by_id(id)
    if message:
        dal.update_message(id, text)
        return 'updated'
    else:
        dal.insert_message(text)
        return 'created'

def delete_message(id: int):
    dal.delete_message(id)

# i.e. @db_try_except
def get_all_messages():
    rows = dal.get_all_messages()
    result = []
    for row in rows:
        result.append(dict(row))
    return result

# **BONUS: can add
# @db_try_except
# def get_message_by_id(id: int):
#     result = dal.get_message_by_id(id)
#     if result:
#         return dict(result)
#     else:
#         return None




