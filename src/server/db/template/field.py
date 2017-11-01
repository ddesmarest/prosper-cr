"""
This module contains all class needed to create user defined fields used in the templates
"""
import uuid
import json
from mongoengine import (EmbeddedDocument, EmbeddedDocumentField,
                        
                        Document, ListField, StringField, DictField, UUIDField)
from types import FACTORY


class UserField(EmbeddedDocument):
    """
    Represents a user field. Field are based on basic types
    """
    name = StringField(required=True)
    tooltip = StringField()
    container = StringField(max_length=100, required=True)
    configuration = DictField()
    uuid = UUIDField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserField, self).__init__(*args, **kwargs)
        self.__container__ = FACTORY.get_type(self.container)

    def initialize(self):
        """
        Should be called after creation
        """
        self.configuration = self.__container__.create_configuration()
        self.uuid = uuid.uuid4()
        self.tooltip = ""
        return self

    def get_containter_type(self):
        """
        Return the type of the field
        """
        return self.__container__

    def validate_configuration(self):
        """
        Validate the configuration using the container
        """
        is_valid, message = self.__container__.validate_configuration(
            self.configuration)
        assert is_valid, message

    def to_dict(self):
        """
        Convert the field into a dict reprentation compatible with json
        """
        return {"id": str(self.uuid),
                "name": str(self.name),
                "tooltip": str(self.tooltip),
                "container": str(self.container),
                "configuration": self.configuration}


class UserFieldGroup(Document):
    """
    Represent a group of user fields
    """
    name = StringField(required=True)
    tooltip = StringField()
    fields = ListField(EmbeddedDocumentField(UserField))

    def save(self, *arg, **args):
        for field in list(self.fields):
            field.validate_configuration()
        super(UserFieldGroup, self).save(arg, args)

    def to_dict(self):
        """
        Convert the group into a dict reprentation compatible with json
        """
        if self.tooltip is None:
            tooltip = ""
        else:
            tooltip = self.tooltip
        fields = []
        for field in self.fields:
            fields.append(field.to_dict())
        return {"id": str(self.id),
                "name": self.name,
                "tooltip": tooltip,
                "fields": fields}
