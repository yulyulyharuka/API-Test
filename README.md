# API-Test

## 1. API for sending a message Just send one parameter string for message After sending should be get response (REST)
### Requirements
1. Python 3.7
2. flask
3. request

### How to Test It
1. pip install all the requirements
2. run first server using `python3 server.py`
3. run second server using `python3 server2/server.py`
4. you can test it using `curl -d 'name=admin' http://127.0.0.1:8082/send`

## 2.  API for collect message that has been sent out API can get all previously sent messages (REST)
### Requirements
1. Python 3.7
2. flask
3. request

### How to Test It
1. pip install all the requirements
2. run first server using `python3 server.py`
3. run second server using `python3 server2/server.py`
4. you can test it using `curl -d http://127.0.0.1:8082/getmessage`

## 3. API for display message in real time API should be long live connection to retrieve messages after send at realtime (Websocket)
### Requirements
1. Python 3.7
2. websockets

### How to Test It
1. pip install all the requirements
2. run server using `python3 WebSocket/server.py`
3. open file client.html in your browser
4. you can test it by type your message in terminal where you run your server
5. see if the message appear in your browser