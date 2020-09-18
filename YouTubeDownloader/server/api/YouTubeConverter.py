from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import pytube

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/converter', methods=['GET', 'POST'])
@cross_origin()
def URL_converter():

    if request.method == "POST":
        url = request.json
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()

        print(video.title)
        video.download("/home/sasha/Downloads", f"{video.title}")
        return "Executed"

    else:
        return send_file(f"/home/sasha/Downloads/{video.title}.mp4", attachment_filename="test.png", as_attachment=True)


@app.route('/getFile')
@cross_origin()
def return_file():
    try:
        return send_file("../../Video/download.jpeg", attachment_filename="test.png", as_attachment=True)

    except Exception as e:
        print(e)
