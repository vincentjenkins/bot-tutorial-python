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
    
    #send text
    def sendmsg(msg):
        url = 'https://api.groupme.com/v3/bots/post'
        postData = {
            'bot_id': '2136fcc43486a18b78d5357206',
            'text': msg,
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=postData, headers=headers)
        print('send url found')
        print(r.status_code)
        print(r.text)
    
    #send image
    def sendimg(img):
        url = 'https://api.groupme.com/v3/bots/post'
        postData = {
            'bot_id': '2136fcc43486a18b78d5357206',
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
    
    # Prevent self-reply
    if data['sender_type'] != 'bot':

        print('not a bot')

        if "you're fucked kid" in data['text'].lower():
            print('sending data')
            sendimg('https://i.groupme.com/1223x1177.jpeg.727b006b9ed441588129373c8d59792a')

        elif "yfk" in data['text'].lower():
            print('sending data')
            sendimg('https://i.groupme.com/1223x1177.jpeg.727b006b9ed441588129373c8d59792a')

        elif "TYLA" in data['text'].upper():
            print('sending data')
            sendmsg('TYLA')

        elif "butler watch" in data['text'].lower():
            print('sending data')
            sendmsg('Tyla looking to repeat at 0-8')
             
        elif "dean" in data['text'].lower():
            print('sending data')
            sendimg('https://i.groupme.com/720x540.jpeg.d36e1e17f89f4895a14ea58854a4ee83')

        elif "legitimately" in data['text'].lower():
            print('sending data')
            sendimg('https://i.groupme.com/692x1263.jpeg.7e8ee27e7da64fc18679c33b0f0b6e91')

        elif "yac" in data['text'].lower():
            print('sending data')
            sendimg('https://i.groupme.com/320x142.gif.68b578a4427545edb7a9f68732c8a9db')

        elif "you're a cuck" in data['text'].lower():
            print('sending data')
            sendimg('https://i.groupme.com/320x142.gif.68b578a4427545edb7a9f68732c8a9db')

    return 'ok', 200




'''def sendmsg(msg):
    url  = 'https://api.groupme.com/v3/groups/71853659/messages'
    print('send url found')
    data = {
        'bot_id': '4e322229309cfb839189723c1d',
        'text': data['name'] + ' pinged me!',
    }
    r = requests.post(url, data=data)#'''
