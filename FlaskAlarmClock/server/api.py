import time
from flask import Flask, request
from flask_cors import CORS, cross_origin

from main import AlarmClock

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/time', methods=['POST'])
@cross_origin()
def get_current_time():
    print("after this")
    print(request.json)
    user_time = request.json
    x = AlarmClock()
    x.set_alarm(user_time)
    return {'time': time.time()}

