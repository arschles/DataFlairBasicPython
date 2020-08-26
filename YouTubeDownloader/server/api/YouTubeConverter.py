from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/converter', methods=['POST'])
@cross_origin()
def URL_converter():
    try:
        data = request.json
        print(data)
        return data
        
    except Exception as e:
        return TypeError("This is just a safe error for testing")

