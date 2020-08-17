from flask import Flask,render_template, url_for
from flask import request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'sweat'

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

  
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return ('<h1>' + form.username.data + ' ' + form.password.data + '</h1>')



    return render_template('login.html', form=form)
    
   

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/terms_of_use', methods = ['GET'])
def terms_of_use():
    return render_template('terms_of_use.html')
 

@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/dashboard', methods = ['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup(): 
    form = RegisterForm()

    if form.validate_on_submit():
         return ('<h1>'+ form.username.data + ' ' + form.email.data + ' ' + form.password.data +'</h1>')
    
    return render_template('signup.html', form=form)





if __name__ == '__main__':
        app.run(port = 7000, debug = True)


