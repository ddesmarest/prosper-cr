"""
This module contains all the handler for user
"""
from flask_restful import Resource, reqparse
from flask import g, request
from server.db.user import User
from server.rest_api.authentification import AUTH
from server.rest_api import create_error_data


class UserAPI(Resource):
    """
    /workspaces handler
    """
    @AUTH.login_required
    def get(self):
        """
        /user GET handler
        """
        return g.user.to_dict(), 200

    @AUTH.login_required
    def put(self):
        """
        /user PUT handler
        """
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True,
                            help="First name missing", location='json')
        parser.add_argument('last_name', required=True,
                            help="Last name missing", location='json')
        args = parser.parse_args()
        g.user.update(set__first_name=args['first_name'], set__last_name=args['last_name'])
        g.user.reload()
        return g.user.to_dict(), 200
