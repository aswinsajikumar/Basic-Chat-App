from models import Message, session
from flask_socketio import SocketIO, send
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    username = msg['username']
    message = msg['message']

    # Save message to PostgreSQL
    new_message = Message(username=username, message=message)
    session.add(new_message)
    session.commit()

    send({'username': username, 'message': message}, broadcast=True)


# API to retrieve all chat messages
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = session.query(Message).all()
    messages_list = [{"id": msg.id, "username": msg.username, "message": msg.message, "timestamp": msg.timestamp} for msg in messages]
    return jsonify(messages_list)

# API to send a message via POST request
@app.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()

    # Extract 'username' and 'message' from the request body
    username = data.get('username')
    message = data.get('message')

    # Create a new message and save it to the database
    new_message = Message(username=username, message=message)
    session.add(new_message)
    session.commit()

    return jsonify({"message": "Message saved successfully!"}), 201

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
