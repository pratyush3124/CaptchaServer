from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import razorpay
from Site import utility

ENV = 'prod'

my_app = Flask(__name__)

if ENV == 'dev':
    my_app.debug = True
    my_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1ram@localhost/captcha'
else:
    my_app.debug = False
    my_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bpubqeyqhekidv:b33f622dd2ada7f376b44b20a9d025db7f264b3590021df8d50b54ef0f263c6b@ec2-52-44-80-40.compute-1.amazonaws.com:5432/d76hkeledml0ld'

db = SQLAlchemy(my_app)

api_key = "rzp_test_CdqGx08LQ19FSF"
api_secret="ZVmBJCf2gdC6QGwUyszN9Wn0"
rpclient = razorpay.Client(auth=(api_key, api_secret))
ut = utility.Utility(client=rpclient)

from Site import routes
