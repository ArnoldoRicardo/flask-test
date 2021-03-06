from flask import Flask, request, make_response, redirect, render_template, session, jsonify
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

todos = ['tarea 1', 'tarea 2', 'tarea 3', 'tarea 4']


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/home'))
    session['user_ip'] = user_ip

    return response


@app.route('/home')
def home():
    user_ip = session.get('user_ip')

    if not user_ip:
        return redirect('/')

    login_form = LoginForm()

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form
    }

    return render_template('hello.html', **context)


@app.route('/api')
def api():

    return jsonify(todos)


@app.route('/login', methods=['GET', 'POST'])
def login():

    return 'te logueaste'