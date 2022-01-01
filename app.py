from flask import Flask
from flask import url_for, render_template
from flask import request
from flask_cors import CORS
import base64
import io
from PIL import Image
from solver import solve_captcha

app = Flask(__name__)
app.debug = False
CORS(app)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/api", methods=['POST'])
def api():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    img = Image.open(io.BytesIO(decoded))
    solved = solve_captcha(img)

    return {'answer':solved}
