import time
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/test', methods=['POST'])
def test_route():
  test_var = request 
    print(test_var)
