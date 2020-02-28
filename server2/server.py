from flask import Flask, request

app = Flask(__name__)

# list to save all the messages that sent out
messages = {}
messages['message'] = []

@app.route('/receive', methods=['POST'])
def sendMessage() :
    data = request.values
    
    message = ''
    if (data['name'] != None) :
        message = "Hello, " + data['name']
    else :
        message = "Goodbye."
    
    return (message)

if __name__== '__main__' :
    app.run(debug=True, port=8083)