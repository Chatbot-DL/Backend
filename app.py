from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
import ollama

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

import eventlet
eventlet.monkey_patch()

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Flask SocketIO Server Running"

@socketio.on('message')
def handle_message(msg):
    stream = ollama.chat(
        model='chatboot-game',
        messages=[{'role': 'user', 'content': msg}],
        stream=True,
    )
    for chunk in stream:    
        content = chunk['message']['content']
        # print(f"Response: {content}")
        socketio.emit('response', content)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
