""" 
This module contains all class needed to manage user group workspace
"""
import uuid
import json
from mongoengine import Document, ListField, ReferenceField
from server.db.template.field import UserFieldGroup
from server.db.user import User


class Workspace(Document):
    """
    A workspace is a common place shared by a user group
    """

    field_groups = ListField(ReferenceField(UserFieldGroup))
    users = ListField(ReferenceField(User))
