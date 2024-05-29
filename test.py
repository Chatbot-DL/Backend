from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
