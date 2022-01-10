from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import razorpay
from Site import utility

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1ram@localhost/captcha'
db = SQLAlchemy(app)

api_key = "rzp_test_CdqGx08LQ19FSF"
api_secret="ZVmBJCf2gdC6QGwUyszN9Wn0"
rpclient = razorpay.Client(auth=(api_key, api_secret))
ut = utility.Utility(client=rpclient)

from Site import routes
