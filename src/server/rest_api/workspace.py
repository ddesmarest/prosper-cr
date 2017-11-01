"""
This module contains all the handler for workspace
"""
from flask_restful import Resource
from server.db.workspace import Workspace
class Workspaces(Resource):
    """
    /workspaces handler
    """
    def get(self):
        """
        Returns the workspaces
        """
        workspaces = []
        
        for workspace in Workspace.objects():
            workspaces.append(workspace.to_dict())
        return workspaces
