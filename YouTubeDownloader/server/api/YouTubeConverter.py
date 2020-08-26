import flask from Flask
import pytube

app = Flask(__name__)

@app.route('/converter', methods=["POST"])
def URL_converter():
    try:
        data = request.form
        print(data)
        
    except Exception as e:
        return TypeError("This is just a safe error for testing")

