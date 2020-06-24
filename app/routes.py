from app import app
from config import Config

import os

from app.controller import user_controller


@app.route('/')
@app.route('/index')
def index():
    print(os.getenv('SECRET_KEY'))
    return "Hello Maman"

@app.route('/users', methods=['GET'])
def users():
    return user_controller.index()

@app.route('/users', methods=['POST'])
def create_user():
    return user_controller.store()

@app.route('/users/<id>')
def user_detail(id):
    return user_controller.show(id)

@app.route('/users/<id>', methods=['PUT'])
def update(id):
    return user_controller.update(id)

@app.route('/users/<id>', methods=['DELETE'])
def delete(id):
    return user_controller.delete(id)