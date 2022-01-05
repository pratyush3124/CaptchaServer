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
def main():
    return render_template('home.html', a='asdf')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')

@app.route("/terms")
def terms():
    return render_template('terms.html')

@app.route("/refund")
def refund():
    return render_template('refund.html')

@app.route("/pay")
def payment():
    return render_template('payments.html')

@app.route("/payment/success")
def succesfulPayment():
    return "Payment Successful"

@app.route("/api", methods=['POST'])
def api():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    img = Image.open(io.BytesIO(decoded))
    solved = solve_captcha(img)

    return {'answer':solved}
