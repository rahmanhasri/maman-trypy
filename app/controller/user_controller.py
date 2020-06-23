from Flask import request
from app.model.user import Users
from app import app
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
            return response.badRequest(null, 'Empty....')

        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def create():
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')

        new_user = Users(name=name, email=email)
        new_user.set_password(password)
        db.session
    except Exception as e:
        print(e)