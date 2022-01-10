from flask_sqlalchemy import SQLAlchemy
from Site import app, rpclient, ut, db
# from Site.solver import solve_captcha
from Site.models import User
from flask import render_template, request
from flask_cors import cross_origin
# import base64
# import io
# from PIL import Image
import random

rzp_key = "rzp_test_CdqGx08LQ19FSF"


@app.route("/")
def main():
    return render_template('home.html')


@app.route("/aboutus/")
def aboutus():
    return render_template('aboutus.html')


@app.route("/privacy/")
def privacy():
    return render_template('privacy.html')


@app.route("/terms/")
def terms():
    return render_template('terms.html')


@app.route("/refund/")
def refund():
    return render_template('refund.html')


@app.route("/pay/")
def payment():
    args = dict(request.args)
    print(args)
    DATA = {
        "amount": 4500,
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
            "uid": args['uid']
        }
    }
    order = rpclient.order.create(data=DATA)
    return render_template('payments.html', oid=str(order["id"]), uid=args['uid'], key=str(rzp_key))


@app.route("/payment/success/", methods=['POST'])
def succesfulPayment():
    uid = request.args['uid']
    message = request.form
    params_dict = dict(message)
    sig_check = ut.verify_payment_signature(params_dict)
    if sig_check:
        q = User.query.filter_by(userId=uid)
        if q == []:
            return "Payment Failed"
        else:
            user = q[0]
            user.isBought = True
            user.paymentId = params_dict['razorpay_payment_id']
            user.orderId = params_dict['razorpay_order_id']
            db.session.commit()
        return "<h4> Payment Successful! <br> You can close this window now and refresh Vtop</h4>"
    else:
        print("Wrong hash")


@app.route("/api/", methods=['POST'])
@cross_origin()
def api():
    message = request.get_json(force=True)
    print(message)
    func = message['function']
    if func == 'createID':
        return createID()
    elif checkID(message['uid']):
        if func == 'checkBought':
            return checkBought(message['uid'])
    return {}


def checkID(uid):
    q = User.query.filter_by(userId=uid).all()
    return False if q == [] else True


def createID():
    new_id = random.randint(100000, 999999)
    new_user = User(userId=new_id)
    db.session.add(new_user)
    db.session.commit()
    print(f"new user created {new_user}")
    return {'newId': new_id}


def checkBought(uid):
    q = User.query.filter_by(userId=uid).all()
    return {'ans': q[0].isBought}

# @app.route("/ml/predict/", methods=['POST'])
# def ml():
#     message = request.get_json(force=True)
#     encoded = message['image']
#     decoded = base64.b64decode(encoded)
#     img = Image.open(io.BytesIO(decoded))
#     solved = solve_captcha(img)
#     return {'answer':solved}