import os
import requests

from flask import Flask, request

app = Flask(__name__)
data = request.json

@app.route('/', methods=['GET'])
def home():
    return 'You could put any content here you like, perhaps even a homepage for your bot!'


@app.route('/', methods=['POST'])
def receive():
    print('Incoming message:')
    print(data['sender_type'])
    print(data['text'])
    print(data['name'])
    
    # Prevent self-reply
    if data['sender_type'] != 'bot':
        print('not a bot')
        if data['text'].startswith('/ping'):
            def send(msg):
                url  = 'https://api.groupme.com/v3/bots/post'
                print('send url found')
                data = {
                    'bot_id': '4e322229309cfb839189723c1d',
                    'text': data['name'] + ' pinged me!',
                }
                r = requests.post(url, data=data)
            print('sending data')
            send(data['name'] + ' pinged me!')

    return 'ok', 200


'''def send(msg):
    url  = 'https://api.groupme.com/v3/bots/post'
    print('send url found')
    data = {
        'bot_id': '4e322229309cfb839189723c1d',
        'text': data['name'] + ' pinged me!',
    }
    r = requests.post(url, data=data)#'''
