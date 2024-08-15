from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def   
 handle_message(data):
    messages.append(data)
    emit('response', {'data': 'Message received from client'}, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    socketio.run(app)
