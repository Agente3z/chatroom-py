from flask import Flask,request
from flask_socketio import SocketIO
from register import register
from login import login
import cookiepy

app = Flask(__name__)   # create the Flask app
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.post('/')
def post():
    if request.form['method'] == 'register':
        username = request.form['username']
        password = request.form['password']
        return register(username, password)

    if request.form['method'] == 'login':
        username = request.form['username']
        password = request.form['password']
        if login(username, password) == "Login successful":
            return cookiepy.generateCookie(username)
        else:
            return "Login failed"

    if request.form['method'] == 'send':
        cookie = request.form['cookie']
        username = request.form['username']
        with open('data/cookies/'+username, 'r') as f:
            if f.read() == cookie:
                msg = request.form['msg']
                with open('data/messages.txt', 'a') as f:
                    f.write(username + ':' + msg + '\n')
                return "Message sent"
            else:
                return "Invalid cookie"

    if request.form['method'] == 'get':
        with open('data/messages.txt', 'r') as f:
            return f.read()

@socketio.on('message')
def on_msg():
    socketio.emit('Incoming message')

if __name__ == '__main__':
    socketio.run(app, debug=True)