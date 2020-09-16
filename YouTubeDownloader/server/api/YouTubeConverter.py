from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import pytube

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/converter', methods=['GET','POST'])
@cross_origin()
def URL_converter():

    if request.method == "POST":
        url_1 = request.json
        print(url_1)
        url_2 = str(url_1)
        print(type(url_2))
            # url =request.get_json()
            # url = request.form["url"]
            # print(url)
        url = 'https://www.youtube.com/watch?v=tXOIvjbNhts'
        print(type(url))
        youtube = pytube.YouTube(url_2)
            # video = youtube.streams.first()

            # video.download("../../Video",f"{video.title}.mp4")

            # return send_file("../../Video/download.jpeg",attachment_filename="test.png",as_attachment=True)

        return send_file("../../Video/download.jpeg",attachment_filename="test.png",as_attachment=True)
    else:
        return "this fuckign sucks"



@app.route('/getFile')
@cross_origin()
def return_file():
    try:
        return send_file("../../Video/download.jpeg",attachment_filename="test.png",as_attachment=True)

    except Exception as e:
        print(e)
