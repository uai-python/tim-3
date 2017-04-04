from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Pemain(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	usia = db.Column(db.Integer)
	jeniskelamin = db.Column(db.String(10))
	area = db.Column(db.String(20))
	main = db.relationship('SoalDiJawab', backref='user', lazy='dynamic')
	def __init__(self, usia, jeniskelamin, area):
		self.usia = usia
		self.jeniskelamin = jeniskelamin
		self.area = area
	def __repr__(self):
		return '<Area %r>' % self.area

class SoalDiJawab(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	idpemain = db.Column(db.Integer, db.ForeignKey('pemain.id'))
	idsoal = db.Column(db.Integer, db.ForeignKey('soal.id'))
	jawabanpemain = db.Column(db.String(50))
	waktujawab = db.Column(db.Time)
	def __init__(self, idpemain, idsoal, jawabanpemain, waktujawab):
		self.idpemain = idpemain
		self.idsoal = idsoal
		self.jawabanpemain = jawabanpemain
		self.waktujawab = waktujawab
	def __repr__(self):
		return '<Jawaban: %r>' % self.jawabanpemain


class Soal(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pertanyaan = db.Column(db.String(1000))
	jawaban = db.Column(db.String(50))
	soal_di_jawab = db.relationship('SoalDiJawab', backref='jawabansoal', lazy='dynamic')
	def __init__(self, pertanyaan, jawaban):
		self.pertanyaan = pertanyaan
		self.jawaban = jawaban
	def __repr__(self):
		return '<Soal: %r>' % self.pertanyaan


