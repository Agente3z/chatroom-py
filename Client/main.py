import requests
import os
from time import sleep
import threading

serverUrl = "http://127.0.0.1:5000"

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('1. Register')
    print('2. Login')
    print('3. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        username = input('Enter username: ')
        password = input('Enter password: ')
        r = requests.post(serverUrl, data={'method': 'register', 'username': username, 'password': password})
    elif choice == '2':
        username = input('Enter username: ')
        password = input('Enter password: ')
        r = requests.post(serverUrl, data={'method': 'login', 'username': username, 'password': password})
        r = r.text
        if r == 'Login failed':
            print('Login failed')
            sleep(2)
        else:
            with open('cookie.txt', 'w') as f:
                f.write(r)
            cookie = r

            def ottieni():
                while True:
                    chat=requests.post(serverUrl, data={'method': 'get'}).text
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(chat)
                    print('Message: ')
                    sleep(0.5)

            t = threading.Thread(target=ottieni)
            t.daemon = True
            t.start()

            while True:
                msg = input()
                with open('cookie.txt', 'r') as f:
                    cookie = f.read()
                r = requests.post(serverUrl, data={'method': 'send', 'cookie': cookie, 'msg': msg, 'username': username})

    elif choice == '3':
        break



    
