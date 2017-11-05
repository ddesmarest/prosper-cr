"""
This module contains all the handler related to the login/logout
"""
import jwt
import datetime
from flask_restful import Resource, reqparse
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
        'id': id
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
        return payload['id']
    except:
        return None


@AUTH.verify_password
def verify_password(username, password):
    id = get_id_from_token(username, AUTH.secret_key)
    if password != 'unused' or id is None:
        g.user = None
    else:
        users = User.objects(id=id)
        if len(users) == 0:
            g.user = None
        else:
            g.user = users[0]
    return g.user is not None


class LoginAPI(Resource):
    """
    /login handler
    """

    def get_timeout(self, args):
        """Return the timeout contained in args if any, default value otherwise
        """
        timeout = args['timeout']
        if timeout is None:
            timeout = 60

        return timeout

    def add_common_parameters(self, parser):
        """Add common parameter to the parser
        """
        parser.add_argument('timeout', required=False, type=int,
                            help="timeout should be an interger representing minutes", location='json')

    def build_result(self, user, args):
        """Return the api data
        """
        return {'token': get_auth_token_for_id(str(user.id), AUTH.secret_key, self.get_timeout(args)),
                'user': user.to_dict()}

    def post(self):
        """
        Verify the user account
        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True,
                            help="user email missing", location='json')
        parser.add_argument('password', required=True,
                            help="user password missing", location='json')
        self.add_common_parameters(parser)
        args = parser.parse_args()
        users = User.objects(email=args['email'])
        if len(users) == 0 or not users[0].check_password(args['password']):
            return {}, 401
        user = users[0]
        return self.build_result(user, args)

    @AUTH.login_required
    def get(self):
        """
        Update the id to get new timeout
        """
        parser = reqparse.RequestParser()
        self.add_common_parameters(parser)
        args = parser.parse_args()
        return self.build_result(g.user, args)
