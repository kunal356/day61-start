from flask import Flask, render_template
from config import SECRET_KEY
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('login.html', form=form, name=name)


if __name__ == '__main__':
    app.run(debug=True)
