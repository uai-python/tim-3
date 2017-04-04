from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from models import Pemain
from forms import RegistrationForm
from models import db

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
@app.route('/register', methods=['GET', 'POST'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
	db.create_all()
        pemain = Pemain(usia=form.usia.data,jeniskelamin=form.jeniskelamin.data, area=form.area.data)
	print pemain.usia
	print pemain
        db.session.add(pemain)
        db.session.commit()
    #    flash('Selamat bermain!')
        #return redirect(url_for(''))

    return render_template('pemain.html', form=form)

if __name__ == "__main__":
	app.run(host='0.0.0.0')

