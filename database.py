from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app2)

class URLs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(200), nullable=False)
    new_url = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return '<URLs %r>' % self.long_url
