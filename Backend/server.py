from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@socketio.on('live')
def index_live(audio_data):
    try:
        with open("audio_as_bytes.txt", 'wb') as f:
            f.write(audio_data)
        return 'Audio data written successfully'
    except Exception as e:
        return 'Error writing audio data: ' + str(e)
    

if __name__ == '__main__':
    socketio.run(app, debug = True)
