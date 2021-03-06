"""
This module contains all class needed to manage user group workspace
"""

from mongoengine import Document, ListField, ReferenceField, StringField
from server.db.template.field import UserFieldGroup
from server.db.user import User


class Workspace(Document):
    """
    A workspace is a common place shared by a user group
    """
    name = StringField(required=True)
    field_groups = ListField(ReferenceField(UserFieldGroup))
    users = ListField(ReferenceField(User))

    def to_dict(self, recursive):
        """
        Convert the workspace into a dict reprentation compatible with json
        """
        if recursive:
            field_groups = [x.to_dict() for x in self.field_groups]
        else:
            field_groups = [{'id': str(x.id), 'name': x.name}
                            for x in self.field_groups]
        return {'id': str(self.id),
                'name': str(self.name),
                'field_groups': field_groups}
