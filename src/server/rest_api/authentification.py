"""
This module contains all the handler related to the login/logout
"""
import jwt
import datetime
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth
from flask import g
from server.db.user import User
AUTH = HTTPBasicAuth()

AUTH.secret_key = 'prosper-cr-is-nice'

def get_auth_token_for_id(id, secret_key, validity_in_minute, validity_in_second=0):
    """
    Generates the Auth Token
    :return: string
    """
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=validity_in_minute, seconds=validity_in_second),
        'iat': datetime.datetime.utcnow(),
        'sub': id
    }
    return jwt.encode(
        payload,
        secret_key,
        algorithm='HS256'
    )


def get_id_from_token(auth_token, secret_key):
    """ return user id or None
    Decodes the auth token
    :param auth_token
    """
    try:
        payload = jwt.decode(auth_token, secret_key)
        return payload['sub']
    except:
        return None


@AUTH.verify_password
def verify_password(username, password):
    id = get_id_from_token(username, AUTH.secret_key)
    if not id is None:
        g.user = User(id=id)
    else:
        users = User.objects(email=username)
        if len(users) == 0 or not users[0].check_password(password):
            g.user = None
        else:
            g.user = users[0]
    return g.user is not None


class Login(Resource):
    """
    /login handler
    """
    @AUTH.login_required
    def post(self):
        """
        Verify the user account
        """
        return {'id': get_auth_token_for_id(str(g.user.id),AUTH.secret_key, 60)}
