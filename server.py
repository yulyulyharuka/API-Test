from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)
messages = {}
messages['message'] = []

@app.route('/send', methods=['POST'])
def send_message() :
    send_data = request.values 

    # Sending the message to http://127.0.0.1:8083/receive
    message = ''
    r = requests.post("http://127.0.0.1:8083/receive", data=send_data)
    if (r.status_code == 200) :
        message = r.text
    else : 
        message = "Data failed to sent"
    return (message)
    
@app.route('/getmessage', methods=['GET'])
def save_message() :
    send_data = "Test"

    today = datetime.now()
    time = datetime.now().time()
    timestamp = str(today) + " " + str(time)
    r = requests.post("http://127.0.0.1:8083/receive2", data=send_data)
    if (r.status_code == 200) :
        # saving the message to list of message
        messages['message'].append((timestamp, send_data))
        return (messages)
    else :
        message = "failed to send message"
        messages['message'].append((timestamp, message))
        return (messages)

if __name__== '__main__' :
    app.run(debug=True, port=8082)