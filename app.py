from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['CORS_ORIGINS'] = ['https://a383cf8f-e551-4a91-a560-df487bd0a5cf-00-8z64ftwuvwm4.picard.replit.dev']  # Replace with your allowed origin


app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)  # This allows all origins

messages = []


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def handle_message(data):
    messages.append(data)
    emit('response', {'data': 'Message received from client'}, broadcast=True)


@socketio.on('connect')
def handle_connect():
    print('Client connected')


if __name__ == '__main__':
    socketio.run(app)
