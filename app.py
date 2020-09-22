from flask import Flask, request, render_template
from flask_cors import CORS
# from database import URLs
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

@app.route('/') # @<var-you-set-to-Flask(__name__)>
def home():
    return render_template('index.html')

@app.route('/results', methods=['GET','POST'])
def results():
    if request.method=='POST':
        user_url=request.form['url']
        # URLs.query.all()
        return render_template('results.html', user_url=user_url)
    else:
        return render_template('results.html', user_url='somestring')

app.run(debug=True)
