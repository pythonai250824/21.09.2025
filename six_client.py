
import requests

BASE_URL = "http://127.0.0.1:9002"

'''
result = requests.get(f"{BASE_URL}/messages")
result.raise_for_status()
print(result.json())

result = requests.get(f"{BASE_URL}/messages/5")

# if there was error in the server -- also raise error her in the client
# result.raise_for_status()

print(result.json())
print(result.status_code)
'''

while True:
    print('hello !')
    print('1. show messages')
    print('2. show message by id')
    print('3. add message')
    print('4. exit')
    try:
        choice = int(input('what you want to do?'))
    except:
        continue
    if choice == 4:
        break
    match choice:
        case 1:
            result = requests.get(f"{BASE_URL}/messages")
            print(result.json())
        case 2:
            id = input('what message id do you want to see?')
            result = requests.get(f"{BASE_URL}/messages/{id}")
            print(result.json())
        case 3:
            text = input('enter message text: ')
            result = requests.post(f"{BASE_URL}/messages?text={text}")
            print(result.json())






