"""
This module contains all the handler for workspace's field groups
"""
from flask_restful import Resource, reqparse
from flask import g, request
from server.db.workspace import Workspace
from server.rest_api.authentification import AUTH
from server.rest_api import create_error_data


class WorkspaceFieldGroupsAPI(Resource):
    """
    /workspaces handler
    """
    @AUTH.login_required
    def get(self,workspace_id):
        """
        Returns the workspace field groups
        """
        try:
            field_groups = []
            for group in Workspace.objects(users=g.user,id=workspace_id)[0].field_groups:
                field_groups.append(group.to_dict())
            return field_groups
        except Exception as e:
            return create_error_data('Cannot get workspace' + workspace_id + ' for user ' + g.user.email, e), 400

