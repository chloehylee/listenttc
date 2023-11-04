from flask import Flask,request
from flask_socketio import SocketIO as socketio

app = Flask(__name__)

@app.route('/')
def main():
    return "hello world";

@socketio.on('audio_data')
def handle_audio(audio_data):
    # Process and send audio data as needed
    socketio.emit('audio_response', audio_data, broadcast=True)



if __name__ == "__main__":
    app.run(debug = True)


