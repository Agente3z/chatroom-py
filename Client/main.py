import requests
import os
from time import sleep
import socketio
from getchar import inputNoEnter

serverUrl = "http://127.0.0.1:5000"
sio = socketio.Client()
sio.connect(serverUrl)

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
        print(r.text)
        sleep(2)
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

            msg = ""

            @sio.on('Incoming message')
            def ottieni():
                global chat
                chat=requests.post(serverUrl, data={'method': 'get'}).text
                os.system('cls' if os.name == 'nt' else 'clear')
                print(chat)
                print('Message:\n> ',end='')
            
            
            ottieni()

            valido = False
            while True:

                while valido != True:
                    msg,inviato,backspace,valido = inputNoEnter(msg)

                valido = False

                if inviato == True:
                    if msg[:6]=='/image':
                        try:
                            os.system(f'python genascii.py --file {msg[7:]} --cols 80')
                            with open('out.txt', 'r') as f:
                                msg = '\n'+f.read()+"\r"
                        except:
                            print('File not found')
                            continue
                    if msg != '':
                        with open('cookie.txt', 'r') as f:
                            cookie = f.read()
                        r = requests.post(serverUrl, data={'method': 'send', 'cookie': cookie, 'msg': msg, 'username': username})
                        msg = ""
                        inviato = False
                        sio.emit('message')

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(chat)
                    print('Message:\n> '+msg,end='')

    elif choice == '3':
        break



    
