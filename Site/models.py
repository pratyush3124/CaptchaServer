from Site import db

class User(db.Model):
    userId = db.Column(db.String, primary_key=True)
    isBought = db.Column(db.Boolean, nullable=False, default=0)
    paymentId = db.Column(db.String, nullable=False, default=0)
    orderId = db.Column(db.String, nullable=False, default=0)

    def __repr__(self):
        return f"User-{self.userId}-{1 if self.isBought else 0}"
