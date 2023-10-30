import os
import requests
import time

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'You could put any content here you like, perhaps even a homepage for your bot!'
    

@app.route('/', methods=['POST'])

def receive():
    data = request.json
    print('Incoming message:')
    print(data['sender_type'])
    print(data['text'])
    print(data['name'])
    
    # Prevent self-reply
    def send(msg):
        url = 'https://api.groupme.com/v3/bots/post'
        postData = {
            'bot_id': '4e322229309cfb839189723c1d',
            'text': msg,
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=postData, headers=headers)
        print('send url found')
        print(r.status_code)
        print(r.text)
    
    def sendimg(img):
        url = 'https://api.groupme.com/v3/bots/post'
        postData = {
            'bot_id': '4e322229309cfb839189723c1d',
            'attachments': [
                {
                    'type': 'image',
                    'url': img,
                }
            ]
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=postData, headers=headers)
        print('send url found')
        print(r.status_code)
        print(r.text)

    if data['sender_type'] != 'bot':
        print('not a bot')
        
        if data['text'].startswith('/ping'):
            print('sending data')
            send(data['name'] + ' pinged me!')
        
        elif data['text'].startswith('TYLA'):
            print('sending data')
            send('TYLA')

        elif data['text'].startswith('image'):
            print('sending data')
            sendimg('https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg')

    return 'ok', 200




'''def send(msg):
    url  = 'https://api.groupme.com/v3/groups/71853659/messages'
    print('send url found')
    data = {
        'bot_id': '4e322229309cfb839189723c1d',
        'text': data['name'] + ' pinged me!',
    }
    r = requests.post(url, data=data)#'''
