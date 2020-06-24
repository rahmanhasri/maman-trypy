from flask import request
from app.model.user import Users
from app import app, db
from app.lib import response


def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }

    return data

def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email
        })
    return array

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest(None, 'Empty....')

        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def store():
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')

        new_user = Users(name=name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        data = singleTransform(new_user)
        return response.ok(data, 'Successfully create data!')
    except Exception as e:
        print(e)

def update(id):
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        new_password = request.json.get('new_password')
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest(None, 'Empty...')

        # print('HERE YO')
        if user.check_password(password) is False:
            return response.badRequest(None, 'Wrong password')

        user.name = name
        user.email = email
        user.set_password(new_password)
        db.session.commit()
        data = singleTransform(user)
        return response.ok(data, "Successfully updated user with id: {}".format(id))
    except Exception as e:
        print(e)

def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest(None, 'Empty...')
        db.session.delete(user)
        db.session.commit()

        return response.ok({ "id": id }, 'Successfully delete data!')
    except Exception as e:
        print(e)