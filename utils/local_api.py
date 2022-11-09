from flask import Flask, Response, request
from pubsub import pub

app = Flask(__name__)

@app.route('/')
def index():
    return 'test'

@app.route('/control', methods=['POST'])
def control():
    pub.sendMessage('api_control', command=request.json['command'], payload=request.json['payload'])
    return 'recv'
