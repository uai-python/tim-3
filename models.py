from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/nasalsabila/mengenaljakarta/kuisjkt.db'
db = SQLAlchemy(app)

class Pemain(db.Model):
	__tablename__ = 'Pemain'
	id = db.Column(db.Integer, primary_key=True)
	usia = db.Column(db.Integer)
	jeniskelamin = db.Column(db.String(20))
	area = db.Column(db.String(20))
	#main = db.relationship('SoalDiJawab', backref='user', lazy='dynamic')
	def __init__(self, usia, jeniskelamin, area):
		self.usia = usia
		self.jeniskelamin = jeniskelamin
		self.area = area
	def __repr__(self):
		return '<Area %r>' % self.area

class SoalDiJawab(db.Model):
	__tablename__ = 'SoalDiJawab'
	id = db.Column(db.Integer, primary_key=True)
	idpemain = db.Column(db.Integer, db.ForeignKey('pemain.id'))
	idsoal = db.Column(db.Integer, db.ForeignKey('soal.id'))
	jawabanpemain = db.Column(db.Integer)
	waktujawab = db.Column(db.DateTime)
	def __init__(self, idpemain, idsoal, jawabanpemain, waktujawab):
		self.idpemain = idpemain
		self.idsoal = idsoal
		self.jawabanpemain = jawabanpemain
		self.waktujawab = waktujawab
	def __repr__(self):
		return '<Jawaban: %r>' % self.jawabanpemain


class Soal(db.Model):
	__tablename__ = 'Soal'
	id = db.Column(db.Integer, primary_key=True)
	pertanyaan = db.Column(db.String(500))
	jawaban = db.Column(db.Integer)
	#soal_di_jawab = db.relationship('SoalDiJawab', backref='jawabansoal', lazy='dynamic')
	def __init__(self, pertanyaan, jawaban):
		self.pertanyaan = pertanyaan
		self.jawaban = jawaban
	#def __repr__(self):
		return '<Soal: %r>' % self.pertanyaan
