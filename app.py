from flask import Flask, request, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import tempfile
import os.path

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    tempfile.gettempdir(), 'test.db')
db = SQLAlchemy(app)
CORS(app)


class URLs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(200), nullable=False)
    new_url = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return '<URLs %r>' % self.long_url

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['GET','POST'])
def results():
    if request.method=='POST':
        user_url=request.form['url']
        db.session.add(URLs(long_url=user_url))
        db.session.commit()
        check = URLs.query.all()
        print(check)
        return render_template('results.html', user_url=user_url)
    else:
        return render_template('results.html', user_url='somestring')

if __name__ == '__main__':
    app.run(debug=True)
