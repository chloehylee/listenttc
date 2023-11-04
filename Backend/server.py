from flask import Flask,request
import sockets

app = Flask(__name__)

@app.route('/')
def main():
    return "hello world";

@app.route('/connect_to_socket', methods = ['POST'])
def connect_to_socket():
    sockets.connect_to_live_server()



if __name__ == "__main__":
    app.run(debug = True)


