from flask import Flask, request, render_template, redirect
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
        id = URLs.query.filter_by(long_url=user_url).first().id
        newURL = f'http://127.0.0.1:5000/{id}'
        return render_template('results.html', user_url=user_url, new_url=newURL)
    else:
        return render_template('results.html', user_url='somestring')

@app.route('/<int:url_id>', methods=['GET'])
def new_URL(url_id):
    if db.session.query(URLs).filter(URLs.id == url_id).count() == 1:
        url = db.session.query(URLs.long_url).filter(URLs.id == url_id).first()
        return redirect(url[0])
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
