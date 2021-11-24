from flask import *
import json, time
app = Flask(__name__)

@app.route('/')
def data_page():
    data_set ={'name':'Mobic', 'Message':'An online Doctor', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__=="__main__":
    app.run(port=4532)
