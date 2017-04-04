from flask_wtf import Form
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import Required
from wtforms import ValidationError
from models import Pemain

class RegistrationForm(Form):
	usia = IntegerField('Usia', validators=[Required()])
	jeniskelamin = SelectField('Jenis Kelamin', choices=[('l','Laki-Laki'), ('p','Perempuan')])
	area = SelectField('Kota/Kabupaten', choices=[('jaksel','Jakarta Selatan'), ('jakut','Jakarta Utara'), ('jaktim','Jakarta Timur'), ('jakbar','Jakarta Barat'), ('jakpus','Jakarta Pusat'), ('seribu','Kepulauan Seribu')])
	submit = SubmitField('Mulai!')
