""" 
This module contains all class needed to create user defined fields used in the templates
"""
import uuid
import json
from mongoengine import EmbeddedDocument, EmbeddedDocumentField, Document, ListField, StringField, DictField, UUIDField
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

    def to_json(self):
        """
        Convert the field into a json reprentation string
        """
        return '{"id":"%s","name":"%s","tooltip":"%s","container":"%s","configuration":%s}' % (
            str(self.uuid), self.name, self.tooltip,
            self.container, json.dumps(self.configuration))


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

    def to_json(self):
        """
        Convert the group into a json reprentation string
        """
        if self.tooltip is None:
            tooltip = ""
        else:
            tooltip = self.tooltip
        s_field = []
        for field in self.fields:
            s_field.append(field.to_json())
        fields = "[%s]" % (','.join(s_field))
        return '{"id":"%s","name":"%s","tooltip":"%s","fields":%s}' % (str(self.id), self.name, tooltip, fields)
