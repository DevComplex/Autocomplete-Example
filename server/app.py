from flask import Flask, request
from flask_cors import CORS
from json import dumps
from autoCompleteUtil import auto_complete

app = Flask(__name__)
CORS(app)

def get_messages_res(prefix):
    messages = auto_complete(prefix)
    
    res = {
        "autoComplete": {
            "messages": messages
        }
    }

    return res

@app.route("/messages", methods=(["POST"]))
def messages():
    req_body = request.get_json()
    prefix = req_body["prefix"]
    res = get_messages_res(prefix)
    return dumps(res)

if __name__ == "__main__":
    app.run()
    