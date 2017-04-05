from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from models import Pemain
from forms import RegistrationForm
from models import db
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

engine = create_engine('sqlit:///quizdatabase.db', echo=True)
Base = declarative_base()

class Pemain(Base):
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

class SoalDiJawab(Base):
	id = Column(Integer, primary_key=True)
	idpemain = Column(Integer, ForeignKey('pemain.id'))
	idsoal = Column(Integer, ForeignKey('soal.id'))
	jawabanpemain = Column(String(50))
	waktujawab = Column(Time)
	def __init__(self, idpemain, idsoal, jawabanpemain, waktujawab):
		self.idpemain = idpemain
		self.idsoal = idsoal
		self.jawabanpemain = jawabanpemain
		self.waktujawab = waktujawab
	def __repr__(self):
		return '<Jawaban: %r>' % self.jawabanpemain


class Soal(Base):
	id = dColumn(Integer, primary_key=True)
	pertanyaan = Column(String(1000))
	jawaban = Column(String(50))
	soal_di_jawab = relationship('SoalDiJawab', backref='jawabansoal', lazy='dynamic')
	def __init__(self, pertanyaan, jawaban):
		self.pertanyaan = pertanyaan
		self.jawaban = jawaban
	def __repr__(self):
		return '<Soal: %r>' % self.pertanyaan
		
Base.metadata.create_all(engine)

@app.route('/register', methods=['GET', 'POST'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        create_all()
        pemain = Pemain(usia=form.usia.data,jeniskelamin=form.jeniskelamin.data, area=form.area.data)
        session.add(pemain)
        session.commit()
    #    flash('Selamat bermain!')
        #return redirect(url_for(''))

    return render_template('pemain.html', form=form)

if __name__ == "__main__":
	app.run(host='0.0.0.0')

