from flask import Flask, render_template, request, redirect, session
from models import db, Pemain, Soal, SoalDiJawab
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import random

app = Flask(__name__)

app.secret_key = 'LALALALALALA'
app.debug=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/nasalsabila/mengenaljakarta/kuisjkt.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/data", methods=['GET', 'POST'])
def daftar():
	if request.method == 'POST':
		p = Pemain(request.form['usia'], request.form['jeniskelamin'], request.form['area'])
		print p
		db.session.add(p)
		db.session.commit()
		return redirect('/kuis')
	return render_template('formpemain.html')

@app.route("/kuis", methods=['GET'])
def kuis():
	soal = Soal.query.limit(1).all()
	
	return render_template('kuis.html', soal=soal)
	


if __name__ == "__main__":
	app.run(host='0.0.0.0')
