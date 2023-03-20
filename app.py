from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

if os.environ.get("ENV") == "prod":
    client = MongoClient("mongodb+srv://"+os.environ.get("DB_USER")+":"+os.environ.get("DB_PASS")+"@"+os.environ.get("DB_HOST")+"/")
    db = client[os.environ.get("DB_NAME")]
else:
    import mongomock
    client = mongomock.MongoClient()
    db = client['test']

users = db['users']
class User:
    def __init__(self, username, dob, display_name):
        self.username = username
        self.dob = dob
        self.display_name = display_name
    
    def to_dict(self):
        return {
            'username': self.username,
            'dob': self.dob,
            'display_name': self.display_name
        }


def add_user(username, dob, display_name):
    user = User(username, dob, display_name)
    users.insert_one(user.to_dict())

def get_users():
    return list(users.find())

def delete_user(id):
    users.delete_one({'_id': ObjectId(id)})

@app.route('/')
def index():
    user_list = get_users()
    return render_template('index.html', users=user_list)

@app.route('/add', methods=['POST'])
def add():
    username = request.form['username']
    dob = request.form['dob']
    display_name = request.form['display_name']
    add_user(username, dob, display_name)
    return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    obj_id = ObjectId(id)
    delete_user(obj_id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
