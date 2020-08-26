from flask import Flask, request
from flask_cors import CORS, cross_origin
import pytube

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/converter', methods=['POST'])
@cross_origin()
def URL_converter():
    try:
        url = request.json
        print(url)
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        video.download()
        return url

    except Exception as e:
        return TypeError("This is just a safe error for testing")

