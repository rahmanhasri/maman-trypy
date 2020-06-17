# 1 quickstart flask
# activate venv
# after install python dotenv add FLASK_APP=hello.py to .flaskenv
# CMD flask run
from flask import Flask, request, jsonify
from markupsafe import escape
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print(__name__, end='YO!')
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