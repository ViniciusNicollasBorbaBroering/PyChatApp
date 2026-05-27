from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# App and SocketIO initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'pizza'
socketio = SocketIO(app)

# Route
@app.route('/')
def index():
    return render_template('index.html')

# Receive client message
@socketio.on('chat_message')
def handle_chat_message(data):
    print(f"Received message: {data}")
    # Broadcast message to all connected clients
    emit('server_message', data, broadcast=True)

# Run server
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, allow_unsafe_werkzeug=True)