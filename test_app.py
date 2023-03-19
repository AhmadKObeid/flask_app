from app import app, add_user, delete_user, get_users
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def user():
    return {
        'username': 'test_user#',
        'dob': '2000-01-04',
        'display_name': 'Test User222'
    }


def test_add_user(client, user):
    users_before = len(get_users())
    add_user(user['username'], user['dob'], user['display_name'])
    users_after = get_users()
    assert len(users_after) == users_before +1
    assert users_after[-1]['username'] == user['username']
    assert users_after[-1]['dob'] == user['dob']
    assert users_after[-1]['display_name'] == user['display_name']


def test_delete_user(client, user):
    users_before = get_users()
    user_id = str(users_before[-1]['_id'])    
    delete_user(user_id)
    users_after = len(get_users())
    assert users_after == len(users_before) - 1


def test_delete_user_invalid_id(client):
    # Try to delete a user with an invalid ID
    with pytest.raises(Exception):
        delete_user('invalid_id')
