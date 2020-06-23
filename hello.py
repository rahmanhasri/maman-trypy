# 1 quickstart flask
# activate venv
# after install python dotenv add FLASK_APP=hello.py to .flaskenv
# CMD flask run
from flask import Flask, request, jsonify, make_response, render_template, session, redirect, url_for
from dotenv import load_dotenv
from markupsafe import escape
import os

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print(__name__)
    print(os.getenv("SECRET_KEY"))
    return 'Hello, World!'
# Converter types:
# string
# (default) accepts any text without a slash

# int:
# accepts positive integers
# float:
# accepts positive floating point values
# path:
# like string but also accepts slashes
# uuid:
# accepts UUID strings
@app.route('/agent/<int:agent_id>')
def get_agent(agent_id):
    return 'agent with id %d' % agent_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
@app.route('/', methods=['POST'])
def post_hello():
    return jsonify(username=request.json['data'])

@app.route('/home')
def show_home():
    if 'username' in session:
        print(session)
        return 'Welcome %s' % escape(session.get('username'))
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('hello_world'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('show_home'))

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('page_not_found.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp