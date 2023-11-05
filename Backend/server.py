from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap4
import sockets
import whisper

app = Flask(__name__)
LIVE_PORT_SERVER, LIVE_PORT_NUMBER = sockets.start_server()
bootstrap = Bootstrap4(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route("/live_connect", methods = ['GET'])
def live_connect():
    return (LIVE_PORT_SERVER,LIVE_PORT_NUMBER)


if __name__ == "__main__":
    app.run(debug = True)


